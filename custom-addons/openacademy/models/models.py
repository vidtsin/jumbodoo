from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from datetime import timedelta


class Course(models.Model):
    _name = 'openacademy.course'
    _description = 'Openacademy Course'

    name = fields.Char(
        string='Title',
        required=True,
    )
    description = fields.Text(
        string='Description',
    )
    responsible_id = fields.Many2one(
        comodel_name='res.users',
        string="Responsible",
        ondelete='set null',
        index=True,
    )
    session_ids = fields.One2many(
        comodel_name='openacademy.session',
        inverse_name='course_id',
        string='Sessions',
    )
    _sql_constraints = [
        ('name_description_check',
         'CHECK(name != description)',
         "The title of the course should not be the description"),
        ('name_unique',
         'UNIQUE(name)',
         "The course title must be unique"),
    ]

    @api.multi
    def copy(self, default=None):
        default = dict(default or {})
        copied_count = self.search_count(
            [('name', '=like', _(u"Copy of {}%").format(self.name))])
        if not copied_count:
            new_name = _(u"Copy of {}").format(self.name)
        else:
            new_name = _(u"Copy of {} ({})").format(self.name, copied_count)

        default['name'] = new_name
        return super(Course, self).copy(default)


class Session(models.Model):
    _name = 'openacademy.session'
    _description = 'Openacademy Session'

    name = fields.Char(
        string='Name',
        required=True,
    )
    start_date = fields.Date(
        string='Start Date',
        default=fields.Date.today,
    )
    duration = fields.Float(
        string='Duration',
        digits=(6, 2),
        help="Duration in days",
    )
    seats = fields.Integer(
        string='Nuber of seats',
    )
    active = fields.Boolean(
        string='Active',
        default=True,
    )
    color = fields.Integer(
        string='Color'
    )
    instructor_id = fields.Many2one(
        comodel_name='res.partner',
        string="Instructor",
        domain=['|', ('instructor', '=', True),
                ('category_id.name', 'ilike', "Teacher")],
    )
    course_id = fields.Many2one(
        comodel_name='openacademy.course',
        ondelete='cascade',
        string='Course',
        required=True,
    )
    attendee_ids = fields.Many2many(
        comodel_name='res.partner',
        string='Attendees',
    )
    taken_seats = fields.Float(
        string='Taken seats',
        compute='_taken_seats',
    )
    end_date = fields.Date(
        string='End Date',
        compute='_get_end_date',
        inverse='_set_end_date',
        store=True,
    )
    hours = fields.Float(
        string='Duration in hours',
        compute='_get_hours',
        inverse='_set_hours',
    )
    attendees_count = fields.Integer(
        string='Attendees count',
        compute='_get_attendees_count',
        store=True,
    )

    @api.depends('seats', 'attendee_ids')
    def _taken_seats(self):
        for r in self:
            if not r.seats:
                r.taken_seats = 0.0
            else:
                r.taken_seats = 100.0 * len(r.attendee_ids) / r.seats

    @api.onchange('seats', 'attendee_ids')
    def _onchange_seats(self):
        if self.seats < 0:
            return {
                'warning': {
                    'title': _("Invalid value"),
                    'message': _("The number of seats can't be negative"),
                }
            }
        if self.seats < len(self.attendee_ids):
            return {
                'warning': {
                    'title': _("Invalid value"),
                    'message': _("Increase seats or remove excess attendees"),
                }
            }

    @api.depends('start_date', 'duration')
    def _get_end_date(self):
        for r in self:
            if not (r.start_date and r.duration):
                r.end_date = r.start_date
                continue
            duration = timedelta(days=r.duration, seconds=-1)
            r.end_date = r.start_date + duration

    def _set_end_date(self):
        for r in self:
            if not (r.start_date and r.end_date):
                continue
            r.duration = (r.end_date - r.start_date).days + 1

    @api.depends('duration')
    def _get_hours(self):
        for r in self:
            r.hours = r.duration * 24

    def _set_hours(self):
        for r in self:
            r.duration = r.hours / 24

    @api.depends('attendee_ids')
    def _get_attendees_count(self):
        for r in self:
            r.attendees_count = len(r.attendee_ids)

    @api.constrains('instructor_id', 'attendee_ids')
    def _check_instructor_not_in_attendees(self):
        for r in self:
            if r.instructor_id and r.instructor_id in r.attendee_ids:
                raise ValidationError(
                    _("A session's instructor can't be an attendee"))
