from edc_constants.constants import (
    DWTA,
    DONT_KNOW,
    OTHER,
    NONE,
    NO,
    YES,
    MALE,
    FEMALE,
    NEVER)

MALE_FEMALE = (
    (MALE, 'Male'),
    (FEMALE, 'Female')
)

YES_NO = (
    (YES, 'Yes'),
    (NO, 'No')
)

YES_NO_UNSURE = (
    (YES, 'Yes'),
    (NO, 'No'),
    ('UNSURE', 'Unsure')
)

YES_NO_DONTWANT = (
    (YES, 'Yes'),
    (NO, 'No'),
    (DWTA, 'Don\'t want to answer')
)
ARV_USAGE = (
    (YES, 'Yes (confirmed)'),
    ('YES_NOT_CONFIRMED', 'Yes (not confirmed)'),
    (NO, 'No'),
    (DWTA, 'Don\'t want to answer')
)

YES_NO_DNTKNW = (
    (YES, 'Yes'),
    (NO, 'NO'),
    (DONT_KNOW, 'Don\'t Know')
)

ARV_INFLUENCE = (
    (YES, 'Yes'),
    (NO, 'No'),
    ('NEVER_HAD_SEX', 'Never had sex'),
    (DONT_KNOW, 'Don\'t Know')
)

BABY_TEST = (
    ('YES_6_8_WEEK', '6-8 weeks'),
    ('YES_18_MONTHS', '7 weeks - 18 months'),
    (NO, 'NO'),
    (DWTA, 'Don\'t want to answer'),
    (DONT_KNOW, 'Don\'t Know')
)

BABY_TEST_RESULT = (
    ('POSITIVE', 'Positive'),
    ('NEGATIVE', 'Negative'),
    (DWTA, 'Don\'t want to answer'),
    ('DID_NOT_RECIEVE_RESULTS', 'Did not recieve result')
)

ANTE_NATAL_TEST_RESULT = (
    ('POSITIVE ', 'Positive'),
    ('NEGATIVE', 'Negative'),
    ('INDETERMINATE', 'Indeterminate'),
    (DWTA, 'Don\'t want to answer'),
    ('DID_NOT_RECIEVE_RESULTS', 'Did not recieve reaults'),
    (DONT_KNOW, 'Don\'t Know')
)

BABY_FEEDING = (
    ('FORMULA_EXCLUSIVELY', 'Formula exclusively'),
    ('BREAST_MILK_EXCLUSIVELY', 'Breast milk exclusively'),
    ('FORMULA_AND_BREAST_MILK ', 'Formula and breast milk'),
    ('FORMULA_AND_SOLID_FOOD', 'Formula and solid food'),
    ('BREAST_MILK_AND_SOLID_FOOD ', 'Breast milk and solid food'),
    ('FORMULA_BREAST_MILK_AND_SOLID_FOOD',
     'Formula, breast milk and solid food')
)

HIV_TEST_RESULT = (
    ('POSITIVE ', 'Positive'),
    ('NEGATIVE', 'Negative'),
    ('INDETERMINATE', 'Indeterminate'),
    (DWTA, 'Don\'t want to answer'),
    (DONT_KNOW, 'Don\'t Know')
)

EDUCATION = (
    (NONE, 'None'),
    ('NON_FORMAL', 'Non-formal'),
    ('PRIMARY', 'Primary'),
    ('JUNIOR_SECONDARY', 'Junior secondary'),
    ('SENIOR_SECONDARY', 'Senior secondary'),
    ('HIGHER', 'Higher')
)

EMPLOYMENT_STATUS = (
    ('FULL_TIME', 'Full-time employed'),
    ('SELF', 'Self employed'),
    ('PART_TIME', 'Part-time employed'),
    ('OWN', 'Working at own lands/Cattlepost'),
    ('ACTIVELY_SEEKING_WORK', 'Activiley seeking work'),
    ('TOO_OLD_TO_WORK', 'Too old to work'),
    ('PENSIONER', 'Pensioner'),
    ('STUDENT', 'Student'),
    (OTHER, 'Other, specify'),
)

MINE_OCCUPATION = (
    ('LOADER', 'Loader'),
    ('BLASTER', 'Blaster'),
    ('SHAFTMAN', 'Shaftman'),
    ('FOREMAN', 'Foreman'),
    ('DRILLER', 'Driller'),
    (OTHER, 'Other, specify'),
)

COMMODITY = (
    ('QUARRY', 'Quarry'),
    ('COAL', 'Coal'),
    ('KIMBERLITE', 'Kimberlite'),
    ('COPPER_NICKLE', 'Copper/Nickle'),
    ('ASBESTOS', 'Asbestos'),
    (OTHER, 'Other, specify'),
)

CONDOM_CONSENT = (
    ('FEAR_OF_NEEDLES', 'Fear of needles'),
    ('FEAR_OF_HIV_TEST_RESULTS', 'Fear of HIV test results'),
    ('FEAR_OF_HIV_INFECTION', 'Fear of HIV infection'),
    ('NOT_ELIGIBLE', 'Not eligible'),
    ('NO_INCENTIVES', 'No incentives'),
    ('LACK_OF_KNOWLEGDE', 'Lack of knowledge'),
    (OTHER, 'Other, specify'),
)

RELIGION = (
    ('CHRISTIANITY', 'Christianity'),
    ('ISLAM', 'Islam'),
    ('BAHAI', 'Bahai'),
    ('HINDUISM', 'Hinduism'),
    ('BADIMO', 'Badimo'),
    ('NO', 'No Religion'),
    (OTHER, 'Other, specify'),
)

TREATMENT_OPTIONS = (
    ('ANTIRETROVIRALS', 'ANtiretrovirals'),
    ('TRADITIONAL_HEALING', 'Traditional healing'),
    ('SPIRITUAL_HEALING', 'Spiritual healing'),
    ('HERBAL', 'Herbal'),
    (NONE, 'None'),
)


ARV_USES = (
    ('CURE_AIDS', 'Cure AIDS'),
    ('CURE_HIV', 'Cure HIV'),
    ('SUPPRESS_HIV', 'Suppress HIV'),
    (DONT_KNOW, 'Don\'t Know')
)

REASONS_ARV_NOT_TAKEN = (
    ('NON_DISCLOSURE_TO_PARTNER', 'Non disclosure to partner'),
    ('SPRITUALIST_SAID_I_AM_HEALED', 'Spiritualist said I am healed'),
    ('DID_NOT_WANT_TO_BE_CONFINED_TO_MEDICATION',
     'Did not want to be confined to medication'),
    (OTHER, 'Other, specify'),
)

MARITAL_STATUS = (
    ('NEVER', 'Never married'),
    ('MARRIED', 'Married'),
    ('LIVING TOGETHER', 'Living together'),
    ('SEPARATED', 'Separated'),
    ('DIVORCED', 'Divorced'),
    ('WIDOWED', 'Widowed')
)

SPOUSE_VISIT = (
    ('DAILY', 'Daily'),
    ('WEEKLY', 'Weekly'),
    ('FORTNIGHTLY', 'Fortnightly'),
    ('MONTHLY', 'Monthly'),
    ('QUARTELY', 'Quartely'),
    ('YEARLY', 'Yearly'),
    (NEVER, 'Never')
)

TRANSMISSION_PREVENTION = (
    ('ANTIRETROVIRAL_THERAPY',
     'Antiretroviral Therapy (AZT, Drugs before birth)'),
    ('CAESAREAN_SECTION', 'Caesarean section'),
    (DONT_KNOW, 'Don\'t Know')
)

ARV_CONCERN = (
    ('LESS_CONCERNED ', 'Less concerned'),
    ('MORE_CONCERNED ', 'More concerned '),
    (DONT_KNOW, 'Don\'t Know')
)

SEXUAL_BEHAVIOUR = (
    ('LESS_CONDOM_USE', 'Less condom use'),
    ('MORE_CONDOM_USE', 'More condom use'),
    ('LESS_SEXUAL_PARTNERS', 'Less sexual partners'),
    ('MORE_SEXUAL_PARTNERS', 'More sexual partners'),
    ('CONTINUE_TO_PRACTICE_MULTIPLE_AND_CONCURRENT_PARTNERSHIPS',
     'Continue to practice multiple and concurrent partnerships'),
    ('DISCONTINUE_TO_PRACTICE_MULTIPLE_AND_CONCURRENT_PARTNERSHIPS',
     'Discontinue to practice multiple and concurrent partnerships'),
    ('ABSTINENCE', 'Abstinence'),
    (DONT_KNOW, 'Don\'t Know')
)

TB_INFECTION = (
    ('ANYBODY', 'Anybody'),
    ('ONLY_POOR_PEOPLE', 'Only poor people'),
    ('ONLY_HOMELESS_PEOPLE', 'Only homeless people'),
    ('ONLY_ALCOHOLICS', 'Only alcoholics'),
    ('ONLY_DRUG_USERS', 'Only drug users'),
    ('ONLY_PEOPLE_LIVING_WITH_HIV_AND_AIDS',
     'Only people living with HIV/AID'),
    ('ONLY_PEOPLE_WHO_HAVE_BEEN_IN_PRISON',
     'Only people who have been in prison'),
    (DONT_KNOW, 'Don\'t Know')
)

TB_SPREAD = (
    ('SHARING_A_MEAL', 'Sharing a meal'),
    ('HUGGING', 'Hugging'),
    ('SHARING_CLOTHES', 'Sharing clothes'),
    ('SEX_WITH_A_WOMAN_WHO_MISCARRIED',
     'sex with a woman who miscarried'),
    ('SEX_WITH_A_WIDOWER', 'Sex with a widower'),
    ('BORN_IN_A_FAMILY_WITH_HIV', 'Born in a family with HIV'),
    ('HANDSHAKE', 'Handshake'),
    ('TOUCHING_ITEMS_IN_PUBLIC_PLACES ',
     'Touching items in public places(Door knobs, etc.)'),
    (DONT_KNOW, 'Don\'t Know'),
    (OTHER, 'Other, specify'),
)

TB_CURE = (
    ('HERBAL_REMEDIES', 'Herbal remedies'),
    ('HOME_REST_WITHOUT_MEDICINE', 'Home rest without medicine'),
    ('PRAYNG', 'Praying'),
    ('SPECIFIC_DRUGS_GIVEN_BY_HEALTH_CENTER',
     'Specific drug given by health center'),
    ('DOTS', 'DOTS')
)

TESTING_REASONS = (
    ('ILLNESS ', 'Illness'),
    ('PREGNANCY ', 'Pregnancy'),
    ('WANTED_TO_HAVE_A_CHILD', 'Wanted to have a child'),
    ('HAD_UNPROTECTED_SEX', 'Had unprotected sex'),
    ('RAPE', 'Rape'),
    ('PRE_MARITAL_NEW_PARTNER', 'Pre-marital/New partner'),
    ('JUST_WANTED_TO_KNOW', 'Just wanted to know'),
    ('NEEDLE_PRICK', 'Needle prick'),
    ('ENCOURAGED_BY_SOMEONE', 'Encouraged by someone'),
    ('PRE_EMPLOYMENT_SCHOLARSHIP_REQUIREMENTS ',
     'Pre-employment/Scholarship requirements'),
    (DONT_KNOW, 'Don\'t Know'),
    (OTHER, 'Other, specify'),
)

TB_REACTION = (
    ('FEAR', 'Fear'),
    ('SURPRISE', 'Surprise'),
    ('SHAME', 'Shame'),
    ('EMBARASSMENT', 'Embarassment'),
    ('SADNESS_OR_HOPELESSNESS', 'Sadness or hopelessness'),
    (OTHER, 'Other, specify'),
)

REASONS_NOT_TESTED = (
    ('FEAR_OF_KNOWING_MY_STATUS', 'Fear of knowing my status'),
    ('FEAR_MY_PARTNERS_POSSIBLE_REACTION',
     'Fear of my partners possible reaction'),
    ('MY_PARTNER_RECENTLY_TESTED_NEGATIVE',
     'MYy partner recently tested negative'),
    ('FEAR_OF_NEEDLE_PRICK', 'Fear of needle prick'),
    ('I_AM_NOT_AT_RISK', 'I am not at risk'),
    ('I_HAVE_NOT_HAD_THE_TIME_OR_CHANCE_TO_GO_FOR_TESTING',
     'I have not had the time or chance to go for testing'),
    ('JUST_WANTED_TO_KNOW', 'Just wanted to know'),
    ('NEEDLE_PRICK', 'Needle prick'),
    ('ENCOURAGED_BY_SOMEONE', 'Encouranged by someone'),
    ('PRE_EMPLOYMENT_SCHOLARSHIP_REQUIREMENTS ',
     'Pre-employment?Scholarship requirement'),
    ('I_DO_NOT_KNOW_WHERE_TO_GO_TO_GET_TESTED',
     'I do not know where to go to get tested'),
    (OTHER, 'Other, specify'),
)

SMC_SOURCE = (
    ('YOUTH_PROGRAM', 'Youth program'),
    ('TELEVISION_VIDEO', 'Television/Video'),
    ('RADIO', 'Radio'),
    ('NEWSPAPER', 'Newspaper'),
    ('HOSPTAL_CLINIC_VCT', 'Hospital/Clinic/VCT'),
    ('POSTERS_BANNERS_BOOKLET', 'Poster/Banner/Booklet'),
    ('TRADITIONAL_SPIRITUAL_HEALER', 'Tradition/Spiritual healer'),
    ('WORKSHOP_SEMINAR', 'Workshop/Seminar'),
    ('INDIVIDUAL', 'Individual'),
    ('CHURCH', 'Church'),
    ('KGOTLA', 'Kgotla'),
    ('WORKPLACE_PROGRAMME ',
     'Workplace programme ((Peer educator, Counsellor, Co-worker)'),
    ('PEER_EDUCATOR', 'Peer educator'),
    ('SCHOOL', 'School'),
)

TB_INFO_SOURCE = (
    ('YOUTH_PROGRAM', 'Youth program'),
    ('TELEVISION_VIDEO', 'Television/Video'),
    ('RADIO', 'Radio'),
    ('NEWSPAPER', 'Newspaper'),
    ('HOSPTAL_CLINIC_VCT', 'Hospital/Clinic/VCT'),
    ('POSTERS_BANNERS_BOOKLET', 'Poster/Banner/Booklet'),
    ('TRADITIONAL_SPIRITUAL_HEALER', 'Tradition/Spiritual healer'),
    ('WORKSHOP_SEMINAR', 'Workshop/Seminar'),
    ('INDIVIDUAL', 'Individual'),
    ('CHURCH', 'Church'),
    ('KGOTLA', 'Kgotla'),
    ('WORKPLACE_PROGRAMME ',
     'Workplace programme ((Peer educator, Counsellor, Co-worker)'),
    ('PEER_EDUCATOR', 'Peer educator'),
    ('SCHOOL', 'School'),
)

TB_PREVENTION = (
    ('KEEP_WINDOWS_OPEN', 'Keep windows open'),
    ('COVER_YOUR_MOUTH_WHEN_COUGHING',
     'Cover your mouth when coughing'),
    ('AVOID_SHAKING_HANDS', 'Avoid shaking hands'),
    ('GOOD_NUTRITION', 'Good nutrition'),
    ('PRAYING', 'Praying'),
    (DONT_KNOW, 'Don\'t Know')
)


TB_DISCLOSURE = (
    ('SEX_PARTER', 'Sex partner'),
    ('SPOUSE', 'Spouse'),
    ('FRIEND', 'Friend'),
    ('FAMILY_MEMBER', 'Family member(s)'),
    ('OTHER_RELATIVE', 'Other relative(s)'),
    ('HEALTHCARE_WORKER', 'Healthcare worker'),
    ('CO_WORKER', 'Co-worker'),
    (OTHER, 'Other, specify'),
)

HIV_PREVENTION = (
    ('USE_CONDOMS', 'Use condoms'),
    ('HAVE_FEWER_PARTNERS', 'Have fewer partners'),
    ('BOTH_HAVE_PARTNERS', 'Both have partners'),
    ('NO_OTHER_PARTNERS', 'No other partners'),
    ('NO_CASUAL_SEX', 'No casual sex'),
    ('NO_SEX_AT_ALL', 'No sex at all'),
    ('NO_COMMERCIAL_SEX', 'No commercial sex'),
    ('AVOID_INJECTIONS_WITH CONTAMINATED NEEDLES',
     'Avoid injections with contaminated needles'),
    ('AVOID_BLOOD_TRANSFUSIONS', 'Avoid blood transfusions'),
    (DONT_KNOW, 'Don\'t Know')
)

TB_NONDISCLOSURE = (
    ('FEAR_OF_STIGMATISATION', 'Fear of stigmatisation'),
    ('KEEP_IT_A_SECRET', 'Keep it a secret'),
    (OTHER, 'Other, specify'),
)

METHODS_OF_USE = (
    ('SMOKE', 'Smoke'),
    ('SNIFF', 'Sniff'),
    ('CHEW', 'Chew'),
)

SUBSTANCE_FREQUENCY = (
    ('DAILY', 'Daily'),
    ('5_6_DAYS_PER_WEEK', '5-6 Days per week'),
    ('1_4_DAYS_PER_WEEK', '1-4 Days per week'),
    ('1_3_DAYS_PER_MONTH', '1-3 Days per month'),
    ('LESS_THAN_MONTHLY', 'Less than monthly'),

)

SEXUAL_INTERCOURSE_INFLUENCE = (
    ('MARITAL_FULFILMENT', 'Marital fulfilment'),
    ('PERSUASION', 'Persuasion'),
    ('CURIOSITY', 'Curiosity'),
    ('ECONOMIC_REASONS', 'Economic reason'),
    ('RELATIONSHIP_FULFILMENT', 'Relationship fulfilment'),
    ('PEER_PRESSURE', 'Peer pressure'),
    ('OLD_ENOUGH', 'Old enough'),
    (OTHER, 'Other, specify'),
)

SEXUAL_INTERCOURSE_PROTECTION = (
    ('MALE_CONDOMS', 'Male condoms'),
    ('FEMALE_CONDOMS', 'Female condoms'),
    ('MODERN_CONTRACEPTIVES.', 'Modern contraceptives'),
    ('TRADITIONAL_METHODS', 'Traditional methods'),
    ('SPRITUAL_METHODS', 'Spritual methods'),
    (OTHER, 'Other, specify'),
)

SEXUAL_INTERCOURSE_PROTECTION_REASON = (
    ('PREGNANCY', 'Pregnancy'),
    ('HIV', 'HIV'),
    ('STI', 'STI'),
    ('HIV_PREGNANCY', 'HIV/Pregnancy'),
    ('ALL_OF_THE_ABOVE', 'All of the above'),
    (DONT_KNOW, 'Don\'t Know'),
    (OTHER, 'Other, specify'),
)

SEX_PARTNER = (
    ('SPOUSE.', 'Spouse'),
    ('BOYFRIEND_GIRLFRIEND', 'Boyfriend/Girlfriend'),
    ('FAMILY_MEMBER', 'Family member'),
    ('EMPLOYER', 'Employer'),
    ('COLLEAGUE', 'Colleague'),
    ('SUPERVISOR', 'Supervisor'),
    ('STRANGER', 'Stranger'),
    ('FRIEND', 'Friend'),
    (OTHER, 'Other, specify'),
)

ASSISTANCE = (
    ('MEDICAL', 'Medical'),
    ('LEGAL_POLICE', 'Legal/Police'),
    ('SOCIAL', 'Social'),
    ('COUNSELING', 'Counseling'),
    (NONE, 'None'),
    (OTHER, 'Other, specify'),
)

VIOLANCE = (
    ('YES_Pushed', 'YES Pushed or shoved you'),
    ('YES_Choked', 'YES, Choked or burned you'),
    ('YES_Threatened',
     'YES, Threatened or used a gun, knife or other '),
    ('YES_weapon', 'YES, weapon against you'),
    ('YES_Physically',
     'YES, Physically forced you to have sexual'),
    ('YES_intercourse',
     'YES, intercourse against your will'),
    ('YES_Forced',
     'YES, Forced you to do something sexual you found degrading or '
     'humiliating'),
    ('YES_Made_you_afraid',
     'YES, Made you afraid of what would happen if you did not have '
     'sexual intercourse'),
    (NO, 'No'),

)

VIOLANCE_WHO = (
    ('female_partner', 'By an intimate female partner'),
    ('male_partner', 'By an intimate male partner'),
    ('non_intimate_partner', 'By a non-intimate partner'),
)

SERIAL_CONCURRENT = (
    ('concurrent', 'concurrent'),
    ('serial', 'serial'),
)

CONDOM_REASON = (
    ('HIV_STI_PREVENTION ', 'HIV/STI Prevention '),
    ('PREGNANCY_PREVENTION', 'Pregnancy prevention'),
    ('BOTH_HIV_STI_AND_PREGNANCY', 'Both HIV/STI and pregnancy'),
    ('NO_TRUST_OF_PARTNER', 'No trust of partner'),
    ('PARTNER_INSISTED', 'Partner insisted'),
    (DONT_KNOW, 'Don\'t Know')
)

CONDOM_NOT_USED_REASON = (
    ('USE_OTHER', 'Use other family planning methods'),
    ('YOU_OR_YOUR_PARTNER_REFUSED', 'You or your partner refused'),
    ('YOU_OR_YOUR_PARTNER_DRUNK_HIGH_ON_DRUGS',
     'You or your partner drunk/high on drugs'),
    ('IT_REDUCES_PLEASURE', 'It reduces pleasure'),
    ('WE_TRUST_EACH_OTHER', 'We trust each other'),
    (OTHER, 'Other, specify'),
)

CONDOM_PLACE = (
    ('SHOP_PETROL_STATION', 'Shop/Petrol station'),
    ('PHARMACY', 'Pharmacy'),
    ('HOSPITAL_CLINIC', 'Hospital/Clinic'),
    ('BAR/HOTEL_RESTAURANT', 'Bar/Hotel/Restaurant'),
    ('OFFICE_PLACE_OF_WORK', 'Office/Place of work'),
    ('PUBLIC_DISPENSER', 'Public dispenser'),
    ('ANOTHER_PERSON', 'Another person'),
    (DONT_KNOW, 'Don\'t Know'),
    (OTHER, 'Other, specify'),
)

DRUNK_HIGH_SEX = (
    ('YES, I WAS', 'Yes, I was'),
    ('YES, HE/SHE WAS', 'Yes, he/she was'),
    ('YES BOTH OF US', 'Yes both of us'),
    (NO, 'No'),
    (DONT_KNOW, 'Don\'t Know'),
)

CONDOM_PERSUATION = (
    ('YES_ALL_THE_TIME', 'Yes, all the time'),
    ('YES_SOMETIMES', 'Yes, sometimes'),
    (NO, 'No'),
    (DONT_KNOW, 'Don\'t Know')
)

ANTE_NATAL_REASONS = (
    ('DISTANCE FROM HEALTH FACILITY', 'Distance from health fscility'),
    ('LACK OF TRANSPORT', 'Lack of transport'),
    ('POOR SERVICE DELIVERY', 'Poor service delivery'),
    ('DIDN\’T KNOW WHERE TO GO', 'Didn\'t know where to go'),
    ('DIDN\’T UNDERSTAND NEED/BENEFIT',
     'Didn\'t understand need/benefit'),
    ('NO FAMILY/SPOUSE SUPPORT', 'No family/spouse support'),
    (OTHER, 'Other, specify'),
)

CIRCUMICISSION_PLACE = (
    ('GOVT_HEALTH_FACILITY', 'GOVT health facility'),
    ('PRIVATE_HEALTH_FACILITY', 'Private health facility'),
    ('TRADITIONAL', 'Traditional'),
    (DONT_KNOW, 'Don\'t Know')
)

TB_TREATMENT_SOURCE = (
    ('GOVERNMENT_CLINIC', 'Government clinic'),
    ('REFERRAL_OR_DISTRICT_HOSPITAL', 'Referral or district hospital'),
    ('PRIVATE_CLINIC_OR_HOSPITAL', 'Private clinic or hospital'),
    ('PHARMACY_CHEMIST', 'Pharmacy/ Chemist'),
    ('TRADITIONAL_HEALER', 'Traditional healer'),
    (OTHER, 'Other, specify'),
)

ARV_TREATMENT_SOURCE = (
    ('GOVERNMENT_CLINIC', 'Government clinic'),
    ('REFERRAL_OR_DISTRICT_HOSPITAL', 'Referral or district hospital'),
    ('PRIVATE_CLINIC_OR_HOSPITAL', 'Private clinic or hospital'),
    ('PHARMACY_CHEMIST', 'Pharmacy/ Chemist'),
    ('TRADITIONAL_HEALER', 'Traditional healer'),
    (OTHER, 'Other, specify'),
)

TB_TIMES_TREATED = (
    (NONE, 'None'),
    ('ONCE', 'Once'),
    ('TWO_TIMES', 'Two times'),
    ('THREE_TIMES', 'Three tomes'),
    (DONT_KNOW, 'Don\'t Know')
)

TB_SPUTUM_SAMPLE = (
    ('POSITIVE_FOR_TB', 'Positive TB'),
    ('NEGATIVE_FOR_TB', 'Negative for TB'),
    ('AWAITING_RESULTS', 'Awaiting results'),
    (DONT_KNOW, 'Don\'t Know')
)

TB_NO_SPUTUM = (
    ('COULD_NOT_PRODUCE_SPUTUM', 'Could not produce sputum'),
    ('COULD_NOT_GET_TO_THE_CLINIC_OR_HEALTH_CENTRE',
     'Could not get to the clinic or health center'),
    ('I_WAS_NOT_ASKED_TO_SUBMIT_A_SPUTUM_SAMPLE',
     'I was not asked to submit a sputum sample'),
    ('NO_SPUTUM_CONTAINER', 'No sputum container'),
    (OTHER, 'Other, specify'),
)

TB_HELP = (
    ('GOVERNMENT_CLINIC', 'Government'),
    ('REFERRAL_OR_DISTRICT_HOSPITAL',
     'Referral or district hospital'),
    ('PRIVATE_CLINIC_OR_HOSPITAL', 'Private clinic or hospital'),
    ('PHARMACY_CHEMIST', 'Pharmacy/Chemist'),
    ('TRADITIONAL_HEALER', 'Traditional healther'),
    (OTHER, 'Other, specify'),
)

TB_HELP_RESULT = (
    ('I_WAS_PRESCRIBED_CHEST_X_RAY', 'I was prescribed chest X-Ray'),
    ('I_WAS_ASKED_TO_SUBMIT_SPUTUM_SAMPLE',
     'I was asked to submit sputum sample'),
    ('I_WAS_GIVEN_TB_DRUGS', 'I was given TB drugs'),
    ('I_WAS_PRESCRIBED_OTHER_DRUGS', 'I was prescribed other drugs'),
    (OTHER, 'Other, specify'),
)

TB_NO_HELP_REASON = (
    ('NO_M0NEY_FOR_TRANSPORT', 'No money for transport'),
    ('HEALTH_FACILITY_WAS_TOO_FAR', 'Health facility was too far'),
    ('I_DID_NOT_FEEL_SICK_ENOUGH', 'I did not feel sick enough'),
    ('I_COULD_NOT_TAKE_TIME_OFF_WORK',
     'I could not take time off work'),
    (OTHER, 'Other, specify'),
)

CANCER_TEST = (
    ('month', 'A month ago'),
    ('Three_months', 'Three months back'),
    ('Six_months', 'Six months back'),
    ('year', 'A year ago'),
)

HOUSEHOLD_RELATION = (
    ('HEAD', 'Head'),
    ('SPOUSE', 'Spouse'),
    ('SON_DAUGHTER', 'Son/Daughter'),
    ('STEPCHILD', 'Stepchild'),
    ('GRANDCHILD', 'Grandchild'),
    ('PARENT', 'Parent'),
    ('GRANDPARENT', 'Grandparent'),
    ('BROTHER_SISTER', 'Brother/Sister'),
    ('NEPHEW_NIECE', 'Nephew/Niece'),
    ('SON_DAUGHTER IN LAW', 'Son/Daughter in law'),
    ('PARENT_IN_LAW', 'Parent in law'),
    ('OTHER_RELATIVE', 'Other relative'),
    ('NOT_RELATED', 'Not related'),
)

CITIZENSHIP = (
    ('Botswana', 'Botswana'),
    ('Angola', 'Angola'),
    ('Lesotho', 'Lesotho'),
    ('Malawi', 'Malawi'),
    ('Mozambique', 'Mozambique'),
    ('Namibia', 'Namibia'),
    ('SouthAfrica', 'SouthAfrica'),
    ('Swaziland', 'Swaziland'),
    ('Zambia', 'Zambia'),
    ('Zimbabwe', 'Zimbabwe'),
    ('Tanzania', 'Tanzania'),
    ('India', 'India'),
    ('Mauritius', 'Mauritius'),
    ('UK', 'UK'),
    ('USA', 'USA'),
    (OTHER, 'Other, specify'),
)

PERSON_HOUSEHOLD_LIVE = (
    ('Yes_spent_the_night', 'Yes, spent the night'),
    ('Yes_did_not_spend_the_night', 'Yes, did not spend the night'),
    ('No_visitor', 'No, visitor'),
)

ATTENDED_SCHOOL = (
    ('Yes_attending', 'Yes, attending'),
    ('Yes_left', 'Yes, left'),
    (NO, 'No'),
)

STUDY_LEVEL = (
    ('Primary', 'Primary'),
    ('Secondary', 'Secondary'),
    ('Tertiary', 'Tertiary'),
    ('None', 'None'),
    (DONT_KNOW, 'Don\'t Know')
)

UNPAID_REASON = (
    ('Actively_seeking_work', 'Actively seeking work'),
    ('Housework', 'Housework'),
    ('Student', 'Student'),
    ('Too_old_to_work', 'Too old to work'),
    ('Too_sick_to_work', 'Too sick to work'),
    (OTHER, 'Other, specify'),
)

MAIN_WORK = (
    ('Employee_Paid_cash', 'Employee - Paid cash  '),
    ('Employee_Paid_in_kind_only', 'Employee - Paid in kind only  '),
    ('Self_employed_no_employees', 'Self-employed(no employees)  '),
    ('Self_employed_with_employees',
     'Self-employed(with employees)'),
    ('Member_Producer_Cooperatives ',
     'Member - Producer, Cooperatives '),
    ('Unpaid_helper_in_family_business',
     'Unpaid helper in family business'),
    ('Working_at_own_lands_cattlepost',
     'Working at own lands/cattlepost'),
    ('Apprentice', 'Apprentice'),
    ('Volunteer', 'Volunteer'),
)

HELP_RECIEVED = (
    ('COUNSELING', 'Counselling'),
    ('FREE_MEDICINE', 'Free Medicine'),
    ('EXTRA_FOOD', 'Extra money'),
    ('MONEY', 'Money'),
    ('HELP_WITH_TOILETRY', 'Help with toiletry (wheel chairs,'
     'disposable diapers, gloves)'),
    (OTHER, 'Other, specify'),

)

HELP_RECIEVED_FROM = (
    ('RELATIVES', 'Relatives'),
    ('FRIENDS', 'Friends'),
    ('HOSPITAL/CLINIC', 'Hospital/Clinic'),
    ('FBO', 'FBO'),
    ('COMMUNITY ORGANISATIONS', 'Ccommunity organisations'),
    ('NGOs', 'NGOs'),
    ('SPIRITUAL HEALER', 'Spiritual healer'),
    ('WOMENS GROUP', 'Womens group'),
    ('SOCIAL WORKER', 'Social worker'),
    ('TRADITIONAL HEALER', 'Traditional healer'),
    (OTHER, 'Other, specify'),
)

HELP_TYPE = (
    ('COUNSELLING', 'Counselling'),
    ('MONEY', 'Money'),
    ('EXTRA_FOOD', 'Extra food'),
    ('FREE_MEDICINE', 'Free medicine'),
    ('HELP_WITH_CHILDCARE', 'Help with childcare'),
    ('HELP_WITH_SCHOOL_EXPENSES ', 'Help with school expenses'),
    ('INCOME_GENERATING_PROJECTS', 'Income generating projects'),
    ('HELP_WITH_HOUSEWORK', 'Help with housework'),
    ('HELP_WITH_FOOD_PREPARATION', 'Help with food preparations'),
    ('SPIRITUAL_RELIGIOUS_SUPPORT', 'Spiritual/Religious support'),
    ('SUPPORT_GROUP', 'Support group'),
    ('HOSPICE', 'Hospice'),
    (DONT_KNOW, 'Don\'t Know')
)

SATISFACTION_LEVEL = (
    ('VERY_SATISFIED', 'Very satisfied'),
    ('SATISFIED', 'Satisfied'),
    ('NOT_SATISFIED', 'Not Satisfied'),
)

DEATH_AGE = (
    ('AGE', 'Age'),
    (DONT_KNOW, 'Don\'t Know')
)

DEATH_CAUSE = (
    ('AGE', 'Age'),
    ('STOKE', 'Stroke'),
    ('TB', 'TB'),
    ('MALARIA', 'Malaria'),
    ('VIOLENCE_INJURIES', 'Violance/Injuries'),
    ('CAR_ROAD_ACCIDENT', 'Car/Road accident'),
)

TIME_SICK = (
    ('MONTHS', 'Months'),
    (DONT_KNOW, 'Don\'t Know')
)
