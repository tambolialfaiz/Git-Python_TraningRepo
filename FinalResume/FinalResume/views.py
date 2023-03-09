from django.shortcuts import render

def resumePage(request):
    data={
        'title': 'My Resume',
        'contact': 'Contact',
        'contact_info': {
            'address': {
                'place': 'Sangamner',
                'pin_code': '422 605'
            },
            'mobile': '+91 895 622 2832',
            'email': 'Email : alfaiz@baapcompany.com'
        },
        'refr': 'REFERENCES',
        'references': [
            {
                'company_name': 'The BAAP Company',
                'contact_person': 'Rao Sir',
                'phone': '+91 868 9988 686',
                'email':'rao@baapcompany.gmail.com'
            }
        ],
        'personal_info': {
            'name': 'Alfaiz Tamboli',
            'designation': 'Full Stack Developer'
        },
        'experience': [
            {
                'year': '2021-2022',
                'company_name': 'The BAAP Company',
                'description': [
                    'Software Developing',
                    'Developed and maintained web applications using HTML, CSS, JavaScript',
                    'Designed and implemented user interfaces using Bootstrap and ReactJS.'
                ]
            },
            {
                'year': '2022-Present',
                'company_name': 'AIT',
                'description': [
                    'Python',
                    'Django Rest Framework',
                    'Flask API',
                    'MySQL Database, AWS'
                ]
            }
        ],
        'education': [
            {
                'year': '2017-2019',
                'board': 'Savitribai Phule Pune Board',
                'location': 'Pune',
                'degree': '12th',
                'stream': 'Commerce'
            },
            {
                'year': '2019-2022',
                'university': 'Savitribai Phule Pune University',
                'location': 'Pune',
                'degree': 'Bachelor of Commerce'
            }
        ],
        'skills': [
            'Python',
            'Django',
            'ReactJS',
            'Flask',
            'HTML',
            'CSS',
            'JavaScript'
        ],
    }

    return render(request, 'home.html', data)
