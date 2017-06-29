0.16 - 29th June 2017
----------------------
* Updated code to support database schema version 015 (removed unused fields from queries)
* Added new legallyActive query parameter to filter by organisations based on their legally active status
* Improved some SQL queries by removing unnecessary use of UPPER() function


0.15.1 - 8th June 2017
----------------------
* Fix SQL query for single organisation so that primary roles are not duplicated

0.15 - 31st May 2017
--------------------
* Re-organise code structure, remove _site blueprint (now hosted separately) and moved openods_core to openods
* Rename variable API_URL to API_PATH, and remove API_USER and API_PASS variables as they're no longer used
* Update Swagger configuration to move apidocs to /docs underneath api route path (e.g. /api/docs)
* Changes to log formats to improve processing by logging utilties, including splitting URL parameters out into separate KV pairs
* Updated NHS Docker config, removing unecessary files and updating to support new project structure
* Improved 404 handling and logging


0.14 - 4th April 2017
---------------------
* roleCode and primaryRoleCode parameters now take lists of codes (e.g. roleCode=RO177,RO64)
* Added initial Swagger support
* Improved logging to be more useful for monitoring stacks such as Splunk, ELK

0.13 - 22nd March 2017
----------------------
* Added lastUpdatedSince query parameter - returns only records that have changed since the specified date

0.12 - 21st March 2017
----------------------
* Add 'active=True/False' query parameter to /organisations allowing filter by status (Active / Inactive)
* Manifest information on /info now returns all manifest fields, PrimaryRoleScope list, and Record Count
* A few more logging improvements (ongoing job)
* Updated DB schema version to 012 to include new manifest fields and PrimaryRoleScope entries
* App now detects local DEBUG env variable to easily run deployed instances in DEBUG mode
* There is now a hard upper limit of 1000 records - any limit=? request for more than 1000 will be automatically limited to 1000
* Updates to openODS.co.uk documentation pages

0.11 - 16th March 2017
----------------------
* Add postCode query parameter to /organisations [#72](https://github.com/open-ods/open-ods/issues/72)
* Made query parameters case-insensitive [#66](https://github.com/open-ods/open-ods/issues/66)
* Include 'status' field on organisation list [#73](https://github.com/open-ods/open-ods/issues/73)
* Updated DB schema version to 011 to include indexed postcode field on organisations table
* Removed a load of redundant files and code
* Slight improvements to the logging output (more work to do)

0.10 - 10th March 2017
----------------------
* Added support for feature toggle to Docker setup

0.9 - 8th March 2017
--------------------
* Added a feature toggle to hide the PrimaryRole Search hypermedia link
* Updated package dependencies

0.8 - 6th March 2017
--------------------
* Import tool has been moved to its own repository
* Documentation updated with new versions
* 'Try Me' pre-populated JSON has been updated with new schema

0.7 - 3rd March 2017
--------------------
* Updated import tool so that it downloads the schema file as well as the data file when running in download mode
    * NOTE: The auto-download part of the import tool is currently broken in this release due to the data files being moved behind a portal login.
* Updated XML element names and database field names in line with December 2016 XML schema
* Updated OpenODS database schema version to 010
* Added configuration setting for API_URL which allows you to set the path that the API listens on

0.6 - 15th October 2016
-----------------------
Release with latest tweaks ready for forking of project

0.4c - 8th January 2016
---
Remove the 'address' property from address objects in the 'addresses' array.

0.4b - 7th January 2016
---
Fixed typo on 'postalCode' field name.

0.4a - 2nd January 2016
---
Fixed up Procfile for Heroku deployment following refactoring.

0.4 - 2nd January 2016
---
This release is a significant refactor of the code and brings a more tidy API and landing page.

#### Web Site
* Updated landing page, added 'TryIt' page, added simple documentation and guidance for API
* Refactor web site code to be a Flask blueprint [(http://flask.pocoo.org/docs/0.10/blueprints/)](http://flask.pocoo.org/docs/0.10/blueprints/)

#### Core API
* Added all remaining ODS data items to data returned by the API
* Moved all resource endpoints to sit under /api route
* Added CORS support on all /api routes
* Added proper filtering on organisation name using the 'q=' query parameter (and deprecated /organisations/search route)
* Added X-Total-Count for total filtered results returned via /organisations route (to assist with pagination of results)
* Added /api and /api/info routes for additional information about resources and ODS metadata

#### Database
* Significant updates to the import tool which now uses SQLAlchemy to create the database and import the data
* Removed deprecated SQL scripts (due to use of SQLAlchemy in import)

#### Documentation
* Updated docs to reflect new data import method


0.3 - 10th November 2015
---
* Added remaining metadata for roles and relationships
* Added a simple landing page for users arriving at the site
* Added fake /organisations/<ods_code>/endpoints route to demonstrate endpoint repository functionality

0.2 - 6th November 2015
---
* Updated docs to try and help people get started / contribute to the project
* Added some parameters to some routes
* Slightly improved HATEOAS compliance


0.1 - 5th November 2015
---
Initial release of prototype API containing following features:

* View Basic API Documentation
* Search For Organisation By Name
* Get Specific Organisation By ODS Code
* Get List Of Roles
* Basic HATEOAS compliance