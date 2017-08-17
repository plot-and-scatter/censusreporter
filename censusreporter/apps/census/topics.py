## TOPICS ##

'''
Hey, it's a CMS!

Title/slug/description will be used to create the list page at /topics/

Title/description will also be used to create the header on the detail page
at /topics/{{ slug }}/. The contents of an individual page should go inside
{{ template_name }}, which belongs in /templates/topics.

Screenshots of survey questions should be placed in /static/img/questions,
and the filenames listed in {{ question_images }} for each entry.

Possible topics for matching table metadata:

    'topics': ['poverty', 'health insurance', 'marital status', 'citizenship', 'mortgage', 'occupancy', 'education', 'sex', 'public assistance', 'income', 'disability', 'migration', 'housing', 'family type', 'group quarters', 'physical characteristics', 'employment', 'commute', 'tenure', 'place of birth', 'fertility', 'veterans', 'families', 'costs and value', 'language', 'technical', 'roommates', 'children', 'grandparents', 'age', 'race', 'seniors', 'ancestry']
'''
TOPICS_LIST = [
    {
        'title': 'Age and Sex',
        'slug': 'age-sex',
        'topics': ['sex', 'children', 'age', 'seniors'],
        'description': 'How the Census approaches the topics of age and sex.',
        'template_name': 'age_sex.html',
        'question_images': ['age-sex.png',],
        'question_pdfs': [
            ('Age','http://www.census.gov/acs/www/Downloads/QbyQfact/age.pdf'),
            ('Sex','http://www.census.gov/acs/www/Downloads/QbyQfact/sex.pdf')
        ]
    },

    {
        'title': 'Getting Started',
        'slug': 'getting-started',
        'description': "The Census is a big subject and there's a lot to learn, but you don't have to learn it all at once. Here's some help knowing the lay of the land.",
        'short_description': "The Census is a big subject and there's a lot to learn, but you don't have to learn it all at once.",
        'template_name': 'getting_started.html',
    },

]

TOPICS_MAP = { topic['slug']: topic for topic in TOPICS_LIST }

