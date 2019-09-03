git subtree add --prefix=custom-addons/oca-website https://github.com/OCA/website.git 12.0 --squash
./odoo-bin -c odoo.conf --dev=all
