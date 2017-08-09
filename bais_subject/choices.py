MALE_FEMALE = (
    ('MALE', 'MALE'),
    ('FEMALE', 'FEMALE')
)

YES_NO = (
    ('YES', 'YES'),
    ('NO', 'NO')
)

YES_NO_UNSURE = (
    ('YES', 'YES'),
    ('NO', 'NO'),
    ('UNSURE', 'UNSURE')
)

YES_NO_DONTWANT = (
    ('YES', 'YES'),
    ('NO', 'NO'),
    ("DON'T WANT TO ANSWER", "DON'T WANT TO ANSWER")
)
ARV_USAGE = (
    ('YES', 'YES (CONFIRMED)'),
    ('YES', 'YES (NOT CONFIRMED)'),
    ('NO', 'NO'),
    ("DON'T WANT TO TELL", "DON'T WANT TO TELL")
)

YES_NO_DNTKNW = (
    ('YES', 'YES'),
    ('NO', 'NO'),
    ('Don\'t Know', 'Don\'t Know')
)

ARV_INFLUENCE = (
    ('YES', 'YES'),
    ('NO', 'NO'),
    ('NEVER HAD SEX', 'NEVER HAD SEX'),
    ('Don\'t Know', 'Don\'t Know')
)

BABY_TEST = (
    ('YES', '6-8 weeks'),
    ('YES 2', '7 weeks - 18 months'),
    ('NO', 'NO'),
    ('DON’T WANT TO TELL ', 'DON’T WANT TO TELL'),
    ('DON’T KNOW', 'DON’T KNOW')
)

BABY_TEST_RESULT = (
    ('POSITIVE ', 'POSITIVE'),
    ('NEGATIVE', 'NEGATIVE'),
    ('DON’T WANT TO TELL ', 'DON’T WANT TO TELL'),
    ('DID NOT RECIEVE RESULTS', 'DID NOT RECIEVE RESULTS')
)

ANTE_NATAL_TEST_RESULT = (
    ('POSITIVE ', 'POSITIVE'),
    ('NEGATIVE', 'NEGATIVE'),
    ('INDETERMINATE', 'INDETERMINATE'),
    ('DON’T WANT TO TELL ', 'DON’T WANT TO TELL'),
    ('DID NOT RECIEVE RESULTS', 'DID NOT RECIEVE RESULTS'),
    ('DON’T WANT KNOW', 'DON’T WANT KNOW')
)

BABY_FEEDING = (
    ('FORMULA EXCLUSIVELY', 'FORMULA EXCLUSIVELY'),
    ('BREAST MILK EXCLUSIVELY', 'BREAST MILK EXCLUSIVELY'),
    ('FORMULA AND BREAST MILK ', 'FORMULA AND BREAST MILK'),
    ('FORMULA AND SOLID FOOD', 'FORMULA AND SOLID FOOD'),
    ('BREAST MILK EXCLUSIVELY', 'BREAST MILK EXCLUSIVELY'),
    ('BREAST MILK AND SOLID FOOD ', 'BREAST MILK AND SOLID FOOD'),
    ('FORMULA, BREAST MILK AND SOLID FOOD', 'FORMULA, BREAST MILK AND SOLID FOOD')
)

HIV_TEST_RESULT = (
    ('POSITIVE ', 'POSITIVE'),
    ('NEGATIVE', 'NEGATIVE'),
    ('INDETERMINATE', 'INDETERMINATE'),
    ('DON’T WANT TO TELL ', 'DON’T WANT TO TELL'),
    ('DON’T WANT KNOW', 'DON’T WANT KNOW')
)

EDUCATION = (
    ('NONE', 'NONE'),
    ('NON-FORMAL', 'NON-FORMAL'),
    ('PRIMARY', 'PRIMARY'),
    ('JUNIOR SECONDARY', 'JUNIOR SECONDARY'),
    ('SENIOR SECONDARY', 'SENIOR SECONDARY'),
    ('HIGHER', 'HIGHER')
)

EMPLOYMENT_STATUS = (
    ('FULL-TIME', 'FULL-TIME EMPLOYED'),
    ('SELF', 'SELF EMPLOYED'),
    ('PART-TIME', 'PART-TIME EMPLOYED'),
    ('OWN', 'WORKING AT OWN LANDS/CATTLEPOST'),
    ('ACTIVELY SEEKING WORK', 'ACTIVELY SEEKING WORK'),
    ('TOO OLD TO WORK', 'TOO OLD TO WORK'),
    ('PENSIONER', 'PENSIONER'),
    ('STUDENT', 'STUDENT'),
    ('OTHER', 'OTHER')
)

MINE_OCCUPATION = (
    ('LOADER', 'LOADER'),
    ('BLASTER', 'BLASTER'),
    ('SHAFTMAN', 'SHAFTMAN'),
    ('FOREMAN', 'FOREMAN'),
    ('DRILLER', 'DRILLER'),
    ('OTHER', 'OTHER')
)

COMMODITY = (
    ('QUARRY', 'QUARRY'),
    ('COAL', 'COAL'),
    ('KIMBERLITE', 'KIMBERLITE'),
    ('COPPER/NICKLE', 'COPPER/NICKLE'),
    ('ASBESTOS', 'ASBESTOS'),
    ('OTHER', 'OTHER')
)

CONDOM_CONSENT = (
    ('FEAR OF NEEDLES', 'FEAR OF NEEDLES'),
    ('FEAR OF HIV TEST RESULTS', 'FEAR OF HIV TEST RESULTS'),
    ('FEAR OF HIV INFECTION', 'FEAR OF HIV INFECTION'),
    ('NOT ELIGIBLE', 'NOT ELIGIBLE'),
    ('NO INCENTIVES', 'NO INCENTIVES'),
    ('LACK OF KNOWLEGDE', 'LACK OF KNOWLEGDE'),
    ('OTHER', 'OTHER,SPECIFY')
)

RELIGION = (
    ('CHRISTIANITY', 'CHRISTIANITY'),
    ('ISLAM', 'ISLAM'),
    ('BAHAI', 'BAHAI'),
    ('HINDUISM', 'HINDUISM'),
    ('BADIMO', 'BADIMO'),
    ('NO', 'NO RELIGION'),
    ('OTHER', 'OTHER')
)

TREATMENT_OPTIONS = (
    ('ANTIRETROVIRALS', 'ANTIRETROVIRALS'),
    ('TRADITIONAL HEALING', 'TRADITIONAL HEALING'),
    ('SPIRITUAL HEALING', 'SPIRITTUAL HEALING'),
    ('HERBAL', 'HERBAL'),
    ('NONE', 'NONE'),
    ('OTHER', 'OTHER,SPECIFY')
)


ARV_USES = (
    ('CURE AIDS', 'CURE AIDS'),
    ('CURE HIV', 'CURE HIV'),
    ('SUPPRESS HIV', 'SUPPRESS HIV'),
    ('DON’T KNOW', 'DON’T KNOW')
)

REASONS_ARV_NOT_TAKEN = (
    ('NON DISCLOSURE TO PARTNER', 'NON DISCLOSURE TO PARTNER'),
    ('SPRITUALIST SAID I AM HEALED', 'SPRITUALIST SAID I AM HEALED'),
    ('DID NOT WANT TO BE CONFINED TO MEDICATION',
     'DID NOT WANT TO BE CONFINED TO MEDICATION'),
    ('OTHER SPECIFY', 'OTHER SPECIFY'),
)

MARITAL_STATUS = (
    ('NEVER', 'NEVER MARRIED'),
    ('MARRIED', 'MARRIED'),
    ('LIVING TOGETHER', 'LIVING TOGETHER'),
    ('SEPARATED', 'SEPARATED'),
    ('DIVORCED', 'DIVORCED'),
    ('WIDOWED', 'WIDOWED')
)

SPOUSE_VISIT = (
    ('DAILY', 'DAILY'),
    ('WEEKLY', 'WEEKLY'),
    ('FORTNIGHTLY', 'FORTNIGHTLY'),
    ('MONTHLY', 'MONTHLY'),
    ('QUARTELY', 'QUARTELY'),
    ('YEARLY', 'YEARLY'),
    ('NEVER', 'NEVER')
)

TRANSMISSION_PREVENTION = (
    ('ANTIRETROVIRAL THERAPY', 'ANTIRETROVIRAL THERAPY (AZT, DRUGS BEFORE BIRTH)'),
    ('CAESAREAN SECTION', 'CAESAREAN SECTION'),
    ('DON’T KNOW', 'DON’T KNOW'),
    ('OTHER', 'OTHER,SPECIFY')
)

ARV_CONCERN = (
    ('LESS CONCERNED ', 'LESS CONCERNED '),
    ('MORE CONCERNED ', 'MORE CONCERNED '),
    ('DON’T KNOW', 'DON’T KNOW')
)

SEXUAL_BEHAVIOUR = (
    ('LESS CONDOM USE', 'LESS CONDOM USE'),
    ('MORE CONDOM USE', 'MORE CONDOM USE'),
    ('LESS SEXUAL PARTNERS', 'LESS SEXUAL PARTNERS'),
    ('MORE SEXUAL PARTNERS', 'MORE SEXUAL PARTNERS'),
    ('CONTINUE TO PRACTICE MULTIPLE AND CONCURRENT PARTNERSHIPS',
     'CONTINUE TO PRACTICE MULTIPLE AND CONCURRENT PARTNERSHIPS'),
    ('DISCONTINUE TO PRACTICE MULTIPLE AND CONCURRENT PARTNERSHIPS',
     'DISCONTINUE TO PRACTICE MULTIPLE AND CONCURRENT PARTNERSHIPS'),
    ('ABSTINENCE', 'ABSTINENCE'),
    ('DON’T KNOW', 'DON’T KNOW'),
    ('OTHER', 'OTHER, SPECIFY')
)

TB_INFECTION = (
    ('ANYBODY', 'ANYBODY'),
    ('ONLY POOR PEOPLE', 'ONLY POOR PEOPLE'),
    ('ONLY HOMELESS PEOPLE', 'ONLY HOMELESS PEOPLE'),
    ('ONLY ALCOHOLICS', 'ONLY ALCOHOLICS'),
    ('ONLY DRUG USERS', 'ONLY DRUG USERS'),
    ('ONLY PEOPLE LIVING WITH HIV AND AIDS',
     'ONLY PEOPLE LIVING WITH HIV AND AIDS'),
    ('ONLY PEOPLE WHO HAVE BEEN IN PRISON', 'ONLY PEOPLE WHO HAVE BEEN IN PRISON'),
    ('DON’T KNOW', 'DON’T KNOW'),
    ('OTHER', 'OTHER, SPECIFY')
)

TB_SPREAD = (
    ('SHARING A MEAL', 'SHARING A MEAL'),
    ('HUGGING', 'HUGGING'),
    ('SHARING CLOTHES', 'SHARING CLOTHES'),
    ('SEX WITH A WOMAN WHO MISCARRIED', 'SEX WITH A WOMAN WHO MISCARRIED'),
    ('SEX WITH A WIDOWER', 'SEX WITH A WIDOWER'),
    ('BORN IN A FAMILY WITH HIV', 'BORN IN A FAMILY WITH HIV'),
    ('HANDSHAKE', 'HANDSHAKE'),
    ('TOUCHING ITEMS IN PUBLIC PLACES ', 'TOUCHING ITEMS IN PUBLIC PLACES'
     '(Door knobs, etc.)'),
    ('DON’T KNOW', 'DON’T KNOW'),
    ('OTHER', 'OTHER, SPECIFY')
)

TB_CURE = (
    ('HERBAL REMEDIES', 'HERBAL REMEDIES'),
    ('HOME REST WITHOUT MEDICINE', 'HOME REST WITHOUT MEDICINE'),
    ('PRAYNG', 'PRAYING'),
    ('SPECIFIC DRUGS GIVEN BY HEALTH CENTER',
     'SPECIFIC DRUGS GIVEN BY HEALTH CENTER'),
    ('DOTS', 'DOTS')
)

TESTING_REASONS = (
    ('ILLNESS ', 'ILLNESS'),
    ('PREGNANCY ', 'PREGNANCY '),
    ('WANTED TO HAVE A CHILD', 'WANTED TO HAVE A CHILD'),
    ('HAD UNPROTECTED SEX', 'HAD UNPROTECTED SEX'),
    ('RAPE', 'RAPE'),
    ('PRE-MARITAL/ NEW PARTNER', 'PRE-MARITAL/ NEW PARTNER'),
    ('JUST WANTED TO KNOW', 'JUST WANTED TO KNOW'),
    ('NEEDLE PRICK', 'NEEDLE PRICK'),
    ('ENCOURAGED BY SOMEONE', 'ENCOURAGED BY SOMEONE'),
    ('PRE-EMPLOYMENT/SCHOLARSHIP REQUIREMENTS ',
     'PRE-EMPLOYMENT/SCHOLARSHIP REQUIREMENTS '),
    ('DONT KNOW', 'DONT KNOW'),
    ('OTHER', 'OTHER (SPECIFY)'),
)

TB_REACTION = (
    ('FEAR', 'FEAR'),
    ('SURPRISE', 'SURPRISE'),
    ('SHAME', 'SHAME'),
    ('EMBARASSMENT', 'EMBARASSMENT'),
    ('SADNESS OR HOPELESSNESS', 'SADNESS OR HOPELESSNESS'),
    ('OTHER SPECIFIY', 'OTHER SPECIFY'),
)

REASONS_NOT_TESTED = (
    ('FEAR OF KNOWING MY STATUS', 'FEAR OF KNOWING MY STATUS'),
    ('FEAR MY PARTNER’S POSSIBLE REACTION', 'FEAR MY PARTNER’S POSSIBLE REACTION'),
    ('MY PARTNER RECENTLY TESTED NEGATIVE', 'MY PARTNER RECENTLY TESTED NEGATIVE'),
    ('FEAR OF NEEDLE PRICK', 'FEAR OF NEEDLE PRICK'),
    ('I AM NOT AT RISK', 'I AM NOT AT RISK'),
    ('I HAVE NOT HAD THE TIME OR CHANCE TO GO FOR TESTING',
     'I HAVE NOT HAD THE TIME OR CHANCE TO GO FOR TESTING'),
    ('JUST WANTED TO KNOW', 'JUST WANTED TO KNOW'),
    ('NEEDLE PRICK', 'NEEDLE PRICK'),
    ('ENCOURAGED BY SOMEONE', 'ENCOURAGED BY SOMEONE'),
    ('PRE-EMPLOYMENT/SCHOLARSHIP REQUIREMENTS ',
     'PRE-EMPLOYMENT/SCHOLARSHIP REQUIREMENTS '),
    ('I DO NOT KNOW WHERE TO GO TO GET TESTED',
     'I DO NOT KNOW WHERE TO GO TO GET TESTED'),
    ('OTHER', 'OTHER (SPECIFY)'),
)

SMC_SOURCE = (
    ('YOUTH PROGRAM', 'YOUTH PROGRAM'),
    ('TELEVISION/VIDEO', 'TELEVISION/VIDEO'),
    ('RADIO', 'RADIO'),
    ('NEWSPAPER', 'NEWSPAPER'),
    ('HOSPTAL/CLINIC/VCT', 'HOSPITAL/CLINIC/VCT'),
    ('POSTERS/BANNERS/BOOKLET', 'POSTERS/BANNERS/BOOKLET'),
    ('TRADITIONAL/SPIRITUAL HEALER', 'TRADITIONAL/ SPIRITUAL HEALER'),
    ('WORKSHOP/SEMINAR', 'WORKSHOP/SEMINAR'),
    ('INDIVIDUAL', 'INDIVIDUAL'),
    ('CHURCH', 'CHURCH'),
    ('KGOTLA', 'KGOTLA'),
    ('WORKPLACE PROGRAMME ',
     'WORKPLACE PROGRAMME ((PEER EDUCATOR, COUNSELLOR, CO-WORKER)'),
    ('PEER EDUCATOR', 'PEER EDUCATOR'),
    ('SCHOOL', 'SCHOOL'),
    ('OTHER', 'OTHER,SPECIFIY'))

TB_DISCLOSURE = (
    ('SEX PARTER', 'SEX PARTNER'),
    ('SPOUSE', 'SPOUSE'),
    ('FRIEND', 'FRIEND'),
    ('FAMILY MEMBER(S)', 'FAMILY MEMBER(S)'),
    ('OTHER RELATIVE(S)', 'OTHER RElATIVE(S)'),
    ('HEALTHCARE WORKER', 'HEALTHCARE WORKER'),
    ('CO WORKER', 'CO WORKER'),
    ('OTHER', 'OTHER(SPECIFY)')
)

HIV_PREVENTION = (
    ('USE CONDOMS', 'USE CONDOMS'),
    ('HAVE FEWER PARTNERS', 'HAVE FEWER PARTNERS'),
    ('BOTH HAVE PARTNERS', 'BOTH HAVE PARTNERS'),
    ('NO OTHER PARTNERS', 'NO OTHER PARTNERS'),
    ('NO CASUAL SEX', 'NO CASUAL SEX'),
    ('NO SEX AT ALL', 'NO SEX AT ALL'),
    ('NO COMMERCIAL SEX', 'NO COMMERCIAL SEX'),
    ('AVOID INJECTIONS WITH CONTAMINATED NEEDLES',
     'AVOID INJECTIONS WITH CONTAMINATED NEEDLES'),
    ('AVOID BLOOD TRANSFUSIONS', 'AVOID BLOOD TRANSFUSIONS'),
    ('DON/T KNOW ANY', 'DON/T KNOW ANY'),
)

TB_NONDISCLOSURE = (
    ('FEAR OF STIGMASTISATION', 'FEAR OF STIGMATISATION'),
    ('KEEP IT A SECRET', 'KEEP IT A SECRET'),
    ('OTHER', 'OTHER, SPECFIY')
)

METHODS_OF_USE = (
    ('SMOKE', 'SMOKE'),
    ('SNIFF', 'SNIFF'),
    ('CHEW', 'CHEW'),
)

SUBSTANCE_FREQUENCY = (
    ('DAILY', 'DAILY'),
    ('5-6 DAYS PER WEEK', '5-6 DAYS PER WEEK'),
    ('1-4 DAYS PER WEEK', '1-4 DAYS PER WEEK'),
    ('1-3 DAYS PER MONTH', '1-3 DAYS PER MONTH'),
    ('LESS THAN MONTHLY', 'LESS THAN MONTHLY'),

)

SEXUAL_INTERCOURSE_INFLUENCE = (
    ('MARITAL FULFILMENT', 'MARITAL FULFILMENT'),
    ('PERSUASION', 'PERSUASION'),
    ('CURIOSITY', 'CURIOSITY'),
    ('ECONOMIC REASONS', 'ECONOMIC REASONS'),
    ('RELATIONSHIP FULFILMENT', 'RELATIONSHIP FULFILMENT'),
    ('PEER PRESSURE', 'PEER PRESSURE'),
    ('OLD ENOUGH', 'OLD ENOUGH'),
    ('OTHERS', 'OTHERS'),
)

SEXUAL_INTERCOURSE_PROTECTION = (
    ('MALE CONDOMS', 'MALE CONDOMS'),
    ('FEMALE CONDOMS', 'FEMALE CONDOMS'),
    ('MODERN CONTRACEPTIVES.', 'MODERN CONTRACEPTIVES.'),
    ('TRADITIONAL METHODS', 'TRADITIONAL METHODS'),
    ('SPRITUAL METHODS', 'SPRITUAL METHODS'),
    ('OTHER', 'OTHER'),
)

SEXUAL_INTERCOURSE_PROTECTION_REASON = (
    ('PREGNANCY', 'PREGNANCY'),
    ('HIV', 'HIV'),
    ('STI', 'STI'),
    ('HIV/PREGNANCY', 'HIV/PREGNANCY'),
    ('ALL OF THE ABOVE', 'ALL OF THE ABOVE'),
    ('DONT KNOW', 'DONT KNOW'),
    ('OTHER,', 'OTHER,'),
)

SEX_PARTNER = (
    ('SPOUSE.', 'SPOUSE.'),
    ('BOYFRIEND/GIRLFRIEND', 'BOYFRIEND/GIRLFRIEND'),
    ('FAMILY MEMBER', 'FAMILY MEMBER'),
    ('EMPLOYER', 'EMPLOYER'),
    ('COLLEAGUE', 'COLLEAGUE'),
    ('SUPERVISOR', 'SUPERVISOR'),
    ('STRANGER', 'STRANGER'),
    ('FRIEND', 'FRIEND'),
    ('OTHER,', 'OTHER,'),
)

ASSISTANCE = (
    ('MEDICAL', 'MEDICAL'),
    ('LEGAL/POLICE', 'LEGAL/POLICE'),
    ('SOCIAL', 'SOCIAL'),
    ('COUNSELING', 'COUNSELING'),
    ('NONE', 'NONE'),
    ('OTHER', 'OTHER'),
)

VIOLANCE = (
    ('YES Pushed or shoved you', 'YES Pushed or shoved you'),
    ('YES, Choked or burned you', 'YES, Choked or burned you'),
    ('YES, Threatened or used a gun, knife or other ',
     'YES, Threatened or used a gun, knife or other '),
    ('YES, weapon against you', 'YES, weapon against you'),
    ('YES, Physically forced you to have sexual',
     'YES, Physically forced you to have sexual'),
    ('YES, intercourse against your will',
     'YES, intercourse against your will'),
    ('YES, Forced you to do something sexual you found degrading or '
     'humiliating',
     'YES, Forced you to do something sexual you found degrading or '
     'humiliating'),
    ('YES, Made you afraid of what would happen if you did not have '
     'sexual intercourse',
     'YES, Made you afraid of what would happen if you did not have '
     'sexual intercourse'),
    ('No', 'No'),

)

VIOLANCE_WHO = (
    ('By an intimate female partner', 'By an intimate female partner'),
    ('By an intimate male partner', 'By an intimate male partner'),
    ('By a non-intimate partner', 'By a non-intimate partner'),
)

SERIAL_CONCURRENT = (
    ('concurrent', 'concurrent'),
    ('serial', 'serial'),
)

CONDOM_REASON = (
    ('HIV/STI PREVENTION ', 'HIV/STI PREVENTION '),
    ('PREGNANCY  PREVENTION', 'PREGNANCY  PREVENTION'),
    ('BOTH HIV/STI AND PREGNANCY', 'BOTH HIV/STI AND PREGNANCY'),
    ('NO TRUST OF PARTNER', 'NO TRUST OF PARTNER'),
    ('PARTNER INSISTED', 'PARTNER INSISTED'),
    ('DONT KNOW', 'DONT KNOW'),
)

CONDOM_NOT_USED_REASON = (
    ('USE OTHER FAMILY PLANNING METHOD', 'USE OTHER FAMILY PLANNING METHOD'),
    ('YOU OR YOUR PARTNER REFUSED', 'YOU OR YOUR PARTNER REFUSED'),
    ('YOU OR YOUR PARTNER DRUNK/HIGH ON  DRUGS',
     'YOU OR YOUR PARTNER DRUNK/HIGH ON  DRUGS'),
    ('IT REDUCES PLEASURE', 'IT REDUCES PLEASURE'),
    ('WE  TRUST EACH OTHER', 'WE  TRUST EACH OTHER'),
    ('OTHER', 'OTHER'),
)

CONDOM_PLACE = (
    ('SHOP/PETROL STATION', 'SHOP/PETROL STATION'),
    ('PHARMACY', 'PHARMACY'),
    ('HOSPITAL/CLINIC', 'HOSPITAL/CLINIC'),
    ('BAR/HOTEL/RESTAURANT', 'BAR/HOTEL/RESTAURANT'),
    ('OFFICE/PLACE OF WORK', 'OFFICE/PLACE OF WORK'),
    ('PUBLIC DISPENSER', 'PUBLIC DISPENSER'),
    ('ANOTHER PERSON', 'ANOTHER PERSON'),
    ('DONT KNOW', 'DONT KNOW'),
    ('OTHER', 'OTHER'),
)

DRUNK_HIGH_SEX = (
    ('YES, I WAS', 'YES, I WAS'),
    ('YES, HE/SHE WAS', 'YES, HE/SHE WAS'),
    ('YES BOTH OF US', 'YES BOTH OF US'),
    ('NO', 'NO'),
    ('DON’T KNOW', 'DON’T KNOW'),
)

CONDOM_PERSUATION = (
    ('YES, ALL THE TIME', 'YES, ALL THE TIME'),
    ('YES, SOMETIMES', 'YES, SOMETIMES'),
    ('NO', 'NO'),
    ('DONT KNOW', 'DONT KNOW'),
)

ANTE_NATAL_REASONS = (
    ('DISTANCE FROM HEALTH FACILITY', 'DISTANCE FROM HEALTH FACILITY'),
    ('LACK OF TRANSPORT', 'LACK OF TRANSPORT'),
    ('POOR SERVICE DELIVERY', 'POOR SERVICE DELIVERY'),
    ('DIDN’T KNOW WHERE TO GO', 'DIDN’T KNOW WHERE TO GO'),
    ('DIDN’T UNDERSTAND NEED/BENEFIT', 'DIDN’T UNDERSTAND NEED/BENEFIT'),
    ('NO FAMILY/SPOUSE SUPPORT', 'NO FAMILY/SPOUSE SUPPORT'),
    ('OTHERS', 'OTHERS,SPECIFY')
)

CIRCUMICISSION_REASON = (
    ('HIV PREVENTION', 'HIV PREVENTION'),
    ('PEER INFLUENCE', 'PEER INFLUENCE'),
    ('CULTURAL RIGHT', 'CULTURAL RIGHT'),
    ('HYGIENIC REASON', 'HYGIENIC REASON'),
    ('FASHION/COSMETIC', 'FASHION/COSMETIC'),
    ('RELIGION', 'RELIGION'),
    ('SEXUAL PLEASURE', 'SEXUAL PLEASURE'),
    ('PARENTS DECISION', 'PARENTS DECISION'),
    ('MEDICAL REASONS (eg. STI)', 'MEDICAL REASONS (eg. STI)'),
    ('DON’T KNOW', 'DON’T KNOW'),
    ('OTHER ', 'OTHER '),

)

CIRCUMICISSION_PLACE = (
    ('GOVT HEALTH FACILITY', 'GOVT HEALTH FACILITY'),
    ('PRIVATE HEALTH FACILITY', 'PRIVATE HEALTH FACILITY'),
    ('TRADITIONAL', 'TRADITIONAL'),
    ('DON’T KNOW', 'DON’T KNOW'),
)

CIRCUMICISSION_INTENT_REASON = (
    ('HIV PREVENTION', 'HIV PREVENTION'),
    ('PEER INFLUENCE', 'PEER INFLUENCE'),
    ('CULTURAL RIGHT', 'CULTURAL RIGHT'),
    ('HYGIENIC REASON', 'HYGIENIC REASON'),
    ('FASHION', 'FASHION'),
    ('RELIGION', 'RELIGION'),
    ('SEXUAL PLEASURE', 'SEXUAL PLEASURE'),
    ('OTHER', 'OTHER'),
)

CIRCUMICISSION_REJECT_REASON = (
    ('FEAR', 'FEAR'),
    ('CULTURE', 'CULTURE'),
    ('RELIGION', 'RELIGION'),
    ('SPOUSE CONSENT', 'SPOUSE CONSENT'),
    ('PARENTAL CONSENT', 'PARENTAL CONSENT'),
    ('LONG DURATION OF HEALING PERIOD', 'LONG DURATION OF HEALING PERIOD'),
    ('FEAR OF HIV TEST', 'FEAR OF HIV TEST'),
    ('OTHER', 'OTHER'),
)

STI_SYMPTOMS = (
    ('LOWER ABDOMINAL PAIN', 'LOWER ABDOMINAL PAIN'),
    ('OFFENSIVE DISCHARGE/SMELL FROM VAGINA/PENIS',
     'OFFENSIVE DISCHARGE/SMELL FROM VAGINA/PENIS'),
    ('VAGINAL DISCHARGE', 'VAGINAL DISCHARGE'),
    ('ITCHING IN GENITAL AREA', 'ITCHING IN GENITAL AREA'),
    ('BURNING PAIN ON URINATION', 'BURNING PAIN ON URINATION'),
    ('PAIN DURING INTERCOURSE', 'PAIN DURING INTERCOURSE'),
    ('GENITAL ULCERS/OPEN SORES', 'GENITAL ULCERS/OPEN SORES'),
    ('SWELLINGS IN GENITAL AREA', 'SWELLINGS IN GENITAL AREA'),
    ('NO SYMPTOMS', 'NO SYMPTOMS'),
    ('DONT KNOW', 'DONT KNOW'),
    ('OTHER, ', 'OTHER, '),

)

TB_TREATMENT_SOURCE = (
    ('GOVERNMENT CLINIC', 'GOVERNMENT CLINIC'),
    ('REFERRAL OR DISTRICT HOSPITAL', 'REFERRAL OR DISTRICT HOSPITAL'),
    ('PRIVATE CLINIC OR HOSPITAL', 'PRIVATE CLINIC OR HOSPITAL'),
    ('PHARMACY/ CHEMIST', 'PHARMACY/ CHEMIST'),
    ('TRADITIONAL HEALER', 'TRADITIONAL HEALER'),
    ('OTHER, SPECIFY', 'OTHER, SPECIFY'),
)

ARV_TREATMENT_SOURCE = (
    ('GOVERNMENT CLINIC', 'GOVERNMENT CLINIC'),
    ('REFERRAL OR DISTRICT HOSPITAL', 'REFERRAL OR DISTRICT HOSPITAL'),
    ('PRIVATE CLINIC OR HOSPITAL', 'PRIVATE CLINIC OR HOSPITAL'),
    ('PHARMACY/ CHEMIST', 'PHARMACY/ CHEMIST'),
    ('TRADITIONAL HEALER', 'TRADITIONAL HEALER'),
    ('OTHER, SPECIFY', 'OTHER, SPECIFY'),
)

TB_TIMES_TREATED = (
    ('NONE', 'NONE'),
    ('ONCE', 'ONCE'),
    ('TWO TIMES', 'TWO TIMES'),
    ('THREE TIMES', 'THREE TIMES'),
    ('DON’T KNOW', 'DON’T KNOW'),
)

TB_SPUTUM_SAMPLE = (
    ('POSITIVE FOR TB', 'POSITIVE FOR TB'),
    ('NEGATIVE FOR TB', 'NEGATIVE FOR TB'),
    ('AWAITING RESULT', 'AWAITING RESULT'),
    ('DON’T KNOW', 'DON’T KNOW'),
)

TB_NO_SPUTUM = (
    ('COULD NOT PRODUCE SPUTUM', 'COULD NOT PRODUCE SPUTU'),
    ('COULD NOT GET TO THE CLINIC OR HEALTH CENTRE',
     'COULD NOT GET TO THE CLINIC OR HEALTH CENTRE'),
    ('I WAS NOT ASKED TO SUBMIT A SPUTUM SAMPLE',
     'I WAS NOT ASKED TO SUBMIT A SPUTUM SAMPLE'),
    ('NO SPUTUM CONTAINER', 'NO SPUTUM CONTAINER'),
    ('OTHERS,SPECIFY', 'OTHERS,SPECIFY'),
)

TB_HELP = (
    ('GOVERNMENT CLINIC', 'GOVERNMENT CLINIC'),
    ('REFERRAL OR DISTRICT HOSPITAL',
     'REFERRAL OR DISTRICT HOSPITAL'),
    ('PRIVATE CLINIC OR HOSPITAL', 'PRIVATE CLINIC OR HOSPITAL'),
    ('PHARMACY/ CHEMIST', 'PHARMACY/ CHEMIST'),
    ('TRADITIONAL HEALER', 'TRADITIONAL HEALER'),
    ('OTHER, SPECIFY', 'OTHER, SPECIFY'),
)

TB_HELP_RESULT = (
    ('I WAS PRESCRIBED CHEST X RAY', 'I WAS PRESCRIBED CHEST X RAY'),
    ('I WAS ASKED TO SUBMIT SPUTUM SAMPLE', 'I WAS ASKED TO SUBMIT SPUTUM SAMPLE'),
    ('I WAS GIVEN TB DRUGS', 'I WAS GIVEN TB DRUGS'),
    ('I WAS PRESCRIBED OTHER DRUGS', 'I WAS PRESCRIBED OTHER DRUGS'),
    ('OTHER, SPECIFY', 'OTHER, SPECIFY'),
)

TB_NO_HELP_REASON = (
    ('NO M0NEY FOR TRANSPORT', 'NO M0NEY FOR TRANSPORT'),
    ('HEALTH FACILITY WAS TOO FAR', 'HEALTH FACILITY WAS TOO FAR'),
    ('I DID NOT FEEL SICK ENOUGH', 'I DID NOT FEEL SICK ENOUGH'),
    ('I COUND NOT TAKE TIME OFF WORK', 'I COUND NOT TAKE TIME OFF WORK'),
    ('OTHER, SPECIFY', 'OTHER, SPECIFY'),
)

CANCER_TEST = (
    ('A month ago', 'A month ago'),
    ('Three months back', 'Three months back'),
    ('Six months back', 'Six months back'),
    ('A year ago', 'A year ago'),
)

HOUSEHOLD_RELATION = (
    ('HEAD', 'HEAD'),
    ('SPOUSE', 'SPOUSE'),
    ('SON/DAUGHTER', 'SON/DAUGHTER'),
    ('STEPCHILD', 'STEPCHILD'),
    ('GRANDCHILD', 'GRANDCHILD'),
    ('PARENT', 'PARENT'),
    ('GRANDPARENT', 'GRANDPARENT'),
    ('BROTHER/SISTER', 'BROTHER/SISTER'),
    ('NEPHEW/NIECE', 'NEPHEW/NEICE'),
    ('SON/DAUGHTER IN LAW', 'SON/DAUGHTER IN LAW'),
    ('PARENT IN LAW', 'PARENT IN LAW'),
    ('OTHER RELATIVE', 'OTHER RELATIVE'),
    ('NOT RELATED', 'NOT RELTED'),
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
    ('Other', 'Other'),
)

PERSON_HOUSEHOLD_LIVE = (
    ('Yes, spent the night', 'Yes, spent the night'),
    ('Yes, did not spend the night', 'Yes, did not spend the night'),
    ('No, visitor', 'No, visitor'),
)

ATTENDED_SCHOOL = (
    ('Yes, attending', 'Yes, attending'),
    ('Yes, left', 'Yes, left'),
    ('No', 'No'),
)

STUDY_LEVEL = (
    ('Primary', 'Primary'),
    ('Secondary', 'Secondary'),
    ('Tertiary', 'Tertiary'),
    ('None', 'None'),
    ('Don\'t know', 'Don\'t know'),
)

UNPAID_REASON = (
    ('Actively seeking work', 'Actively seeking work'),
    ('Housework', 'Housework'),
    ('Student', 'Student'),
    ('Too old to work', 'Too old to work'),
    ('Too sick to work', 'Too sick to work'),
    ('Other', 'Other'),
)

MAIN_WORK = (
    ('Employee - Paid cash  ', 'Employee - Paid cash  '),
    ('Employee - Paid in kind only  ', 'Employee - Paid in kind only  '),
    ('Self-employed(no employees)  ', 'Self-employed(no employees)  '),
    ('Self-employed(with employees)    ', 'Self-employed(with employees)    '),
    ('Member - Producer, Cooperatives ', 'Member - Producer, Cooperatives '),
    ('Unpaid helper in family business    ',
     'Unpaid helper in family business    '),
    ('Working at own lands/cattlepost   ', 'Working at own lands/cattlepost   '),
    ('Apprentice    ', 'Apprentice    '),
    ('Volunteer', 'Volunteer'),
)

HELP_RECIEVED = (
    ('COUNSELING', 'COUNSELING'),
    ('FREE MEDICINE', 'FREE MEDICINE'),
    ('EXTRA FOOD', 'EXTRA FOOD'),
    ('MONEY', 'MONEY'),
    ('HELP WITH TOILETRY', 'HELP WITH TOILETRY (wheel chairs,'
     'disposable diapers, gloves)'),
    ('OTHERS', 'OTHERS,SPECIFY'),

)

HELP_RECIEVED_FROM = (
    ('RELATIVES', 'RELATIVES'),
    ('FRIENDS', 'FRIENDS'),
    ('HOSPITAL/CLINIC', 'HOSPITAL/CLINIC'),
    ('FBO', 'FBO'),
    ('COMMUNITY ORGANISATIONS', 'COMMUNITY ORGANISATIONS'),
    ('NGOs', 'NGOs'),
    ('SPIRITUAL HEALER', 'SPIRITUAL HEALER'),
    ('WOMENS GROUP', 'WOMENS GROUP'),
    ('SOCIAL WORKER', 'SOCIAL WORKER'),
    ('TRADITIONAL HEALER', 'TRADITIONAL HEALER'),
    ('OTHER', 'OTHER(SPECIFY)'),
)

HELP_TYPE = (
    ('COUNSELLING', 'COUNSELLING'),
    ('MONEY', 'MONEY'),
    ('EXTRA FOOD', 'EXTRA FOOD'),
    ('FREE MEDICINE', 'FREE MEDICINE'),
    ('HELP WITH CHILDCARE', 'HELP WITH CHILDCARE'),
    ('HELP WITH SCHOOL EXPENSES ', 'HELP WITH SCHOOL EXPENSES'),
    ('INCOME GENERATING PROJECTS', 'INCOME GENERATING PROJECTS'),
    ('HELP WITH HOUSEWORK', 'HELP WITH HOUSEWORK'),
    ('HELP WITH FOOD PREPARATION', 'HELP WITH FOOD PREPARATION'),
    ('SPIRITUAL/RELIGIOUS SUPPORT', 'SPIRITUAL/RELIGIOUS SUPPORT'),
    ('SUPPORT GROUP', 'SUPPORT GROUP'),
    ('HOSPICE', 'HOSPICE'),
    ("DON'T KNOW", "DON'T KNOW"),
)

SATISFACTION_LEVEL = (
    ('VERY SATISFIED', 'VERY SATISFIED'),
    ('SATISFIED', 'SATISFIED'),
    ('NOT SATISFIED', 'NOT SATISFIED'),
)

DEATH_AGE = (
    ('AGE', 'AGE'),
    ('DON\'T KNOW', 'DON\'T KNOW'),
)

DEATH_CAUSE = (
    ('AGE', 'AGE'),
    ('STOKE', 'STROKE'),
    ('TB', 'TB'),
    ('MALARIA', 'MALARIA'),
    ('VIOLENCE/INJURIES', 'VIOLENCE/INJURIES'),
    ('CAR/ROAD ACCIDENT', 'CAR/ROAD ACCIDENT'),
)

TIME_SICK = (
    ('MONTHS', 'MONTHS'),
    ('DON\'T KNOW', 'DON\'T KNOW'),
)
