DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',         # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'epiwork',             # Or path to database file if using sqlite3.
        'USER': 'epiwork',         # Not used with sqlite3.
        'PASSWORD': 'iefpi12irbg',     # Not used with sqlite3.
        'HOST': 'localhost',             # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',             # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Madrid'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'es'

# For checking postcodes etc.
# Use ISO3166 two-letter country code
# See http://www.iso.org/iso/country_codes/iso_3166_code_lists/english_country_names_and_code_elements.htm
# Avaliable: be, it, nl, uk, pt, se
COUNTRY = 'es'

# Strict postcode validation with the pollster_zip_codes db table
# Use 'EXACT' to require an exact match in the table, 'NONE' to disable the db check
# Avaliable: NONE, EXACT
POLLSTER_ZIP_CODE_DB_VALIDATION_MODE = 'NONE'

# The shortname of the survey containing the user profile data
# By default for InfluenzaNet websites this is the 'intake' survey
POLLSTER_USER_PROFILE_SURVEY = 'intake'

# The data name of the question in the user profile survey
# used to find a match in the pollster_zip_codes table
# on the zip_code_key column
POLLSTER_USER_ZIP_CODE_DATA_NAME = 'Q3'

# The data name of the question in the user profile survey
# used to match the zip code for the right country
# in the pollster_zip_codes table
POLLSTER_USER_COUNTRY_DATA_NAME = None
