TITLE_CHOICES = (('Mr', 'Mr'),
                 ('Mrs', 'Mrs'),
                 ('Ms', 'Ms'))
GENDER_CHOICES = (('Male', 'M'),
                  ('Female', 'F'))

AFFILIATION_CHOICE_STARTUP = 0
AFFILIATION_CHOICE_DEVELOPER = 1
AFFILIATION_CHOICE_ORGANISATION = 2
AFFILIATION_CHOICE_INDIVIDUAL = 3

AFFILIATION_CHOICES = (
    (AFFILIATION_CHOICE_STARTUP, 'Start-up'),
    (AFFILIATION_CHOICE_DEVELOPER, 'Developer'),
    (AFFILIATION_CHOICE_ORGANISATION, 'Organisation'),
    (AFFILIATION_CHOICE_INDIVIDUAL, 'Individual'),
)

SUBMIT_REASON_PHYSICAL_WORK_SPACE = 0
SUBMIT_REASON_SPACE_TO_HOST_EVENTS = 1
SUBMIT_REASON_BECOME_A_PARTNER = 2
SUBMIT_REASON_PART_OF_COMMUNITY = 3
SUBMIT_REASON_BECOME_A_MENTOR = 4
SUBMIT_REASON_ATTENDING_EVENT = 5

SUBMIT_REASON_CHOICES = (
    (SUBMIT_REASON_PHYSICAL_WORK_SPACE, 'Physical work space'),
    (SUBMIT_REASON_SPACE_TO_HOST_EVENTS, 'Space to host events'),
    (SUBMIT_REASON_BECOME_A_PARTNER, 'To become a partner'),
    (SUBMIT_REASON_PART_OF_COMMUNITY, 'I would just like to be part of the community'),
    (SUBMIT_REASON_BECOME_A_MENTOR, 'To become a mentor'),
    (SUBMIT_REASON_ATTENDING_EVENT, 'Attending an event'),
)

INFORMATION_ABOUT_JOZIHUB_CHOICE_NO = 0
INFORMATION_ABOUT_JOZIHUB_CHOICE_YES = 1

INFORMATION_ABOUT_JOZIHUB_CHOICES = (
    (INFORMATION_ABOUT_JOZIHUB_CHOICE_YES, 'Yes'),
    (INFORMATION_ABOUT_JOZIHUB_CHOICE_NO, 'No'),
)

WHEN_TO_HOST_EVENT_ASAP = 0
WHEN_TO_HOST_EVENT_NEXT_WEEKS = 1
WHEN_TO_HOST_EVENT_NEXT_MONTH = 2
WHEN_TO_HOST_EVENT_NEXT_YEAR = 3

WHEN_TO_HOST_EVENT_CHOICES = (
    (WHEN_TO_HOST_EVENT_ASAP, 'As soon as possible'),
    (WHEN_TO_HOST_EVENT_NEXT_WEEKS, 'During the next few weeks'),
    (WHEN_TO_HOST_EVENT_NEXT_MONTH, 'During the next month'),
    (WHEN_TO_HOST_EVENT_NEXT_YEAR, 'During the next year'),
)

WHEN_TO_GET_ACCESS_IMMEDIATELY = 0
WHEN_TO_GET_ACCESS_NEXT_FEW_WEEKS = 1
WHEN_TO_GET_ACCESS_NEXT_MONTH = 2
WHEN_TO_GET_ACCESS_NEXT_YEAR = 3

WHEN_TO_GET_ACCESS_CHOICES = (
    (WHEN_TO_GET_ACCESS_IMMEDIATELY, 'Immediately'),
    (WHEN_TO_GET_ACCESS_NEXT_FEW_WEEKS, 'During the next few weeks'),
    (WHEN_TO_GET_ACCESS_NEXT_MONTH, 'During the next month'),
    (WHEN_TO_GET_ACCESS_NEXT_YEAR, 'During the next year'),
)

HAPPY_WITH_THE_PRICE_CHOICE_NO = 0
HAPPY_WITH_THE_PRICE_CHOICE_YES = 1

HAPPY_WITH_THE_PRICE_CHOICES = (
    (HAPPY_WITH_THE_PRICE_CHOICE_YES, 'Yes'),
    (HAPPY_WITH_THE_PRICE_CHOICE_NO, 'No'),
)

FIELD_OF_EXPERTISE_DEVELOPING = 0
FIELD_OF_EXPERTISE_ART_AND_DESIGN = 1
FIELD_OF_EXPERTISE_ENTREPRENEURSHIP = 2
FIELD_OF_EXPERTISE_FINANCING_AND_RAISING_CAPITAL = 3
FIELD_OF_EXPERTISE_OTHER = 4

FIELD_OF_EXPERTISE_CHOICES = (
    (FIELD_OF_EXPERTISE_DEVELOPING, 'Developing'),
    (FIELD_OF_EXPERTISE_ART_AND_DESIGN, 'Art and design'),
    (FIELD_OF_EXPERTISE_ENTREPRENEURSHIP, 'Entrepreneurship'),
    (FIELD_OF_EXPERTISE_FINANCING_AND_RAISING_CAPITAL, 'Financing and raising capital'),
    (FIELD_OF_EXPERTISE_OTHER, 'Other'),
)
