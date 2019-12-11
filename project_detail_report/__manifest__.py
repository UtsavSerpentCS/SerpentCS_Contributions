# See LICENSE file for full copyright and licensing details.

{
    # Module Information
    'name': 'Project Report',
    'version': '13.0.1.0.0',
    'category': 'Project Management',
    'license': 'AGPL-3',
    'summary': """Print Project Detail report with task
                    list and task details.""",

    # Author
    'author': 'Serpent Consulting Services Pvt. Ltd.',
    'website': 'http://www.serpentcs.com',
    'maintainer': 'Serpent Consulting Services Pvt. Ltd.',

    # Dependencies
    'depends': [
        'hr_timesheet',
    ],
    # Data
    'data': [
        'views/project_report.xml',
        'report/project_qweb_report.xml',
    ],

    # Technical
    'installable': True,
}
