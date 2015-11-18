from lxml import etree as xml_tree_parser
import os.path
import sys
import zipfile
import logging

log = logging.getLogger('import_ods_xml')
log.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
log.addHandler(ch)


class ODSFileManager(object):

    __ods_xml_data = None

    def __init__(self):
        pass

    def __return_attribute(self, attribute_name):
        pass

    # The purpose of this function is to retrieve the latest published
    # file from a public published location
    def __retrieve_latest_datafile(self):
        # TODO: Retrieve latest file from the local directory until
        # such time it is published and retrievable
        if os.path.isfile('controller/odsfull.xml.zip'):
            log.info('File Found')
            return 'controller/odsfull.xml.zip'
        else:
            raise ValueError('unable to locate the data file')

    # The purpose of this function is to determine if we have a zip
    # for or xml file, check it is valid
    # and then populate an etree object for us to parse
    # TODO: validate the xml file against a schema
    def __import_latest_datafile(self, data_filename):

        try:
            with zipfile.ZipFile(data_filename) as local_zipfile:
                # get to the name of the actual zip file
                # TODO: this is a horrible impementation
                data_filename = data_filename.replace('.zip', '')
                data_filename = data_filename.split('/', 1)
                data_filename = data_filename[1]

                log.info(data_filename)

                with local_zipfile.open(data_filename) as local_datafile:
                    self.__ods_xml_data = xml_tree_parser.parse(local_datafile)

                return True
        except:
            print('Unexpected error:', sys.exc_info()[0])
            raise

    # The purpose of this function is to check if we have odsxml data
    # if we don't it should retrieve the latest version available and
    # explode it from zip format into a xmltree object
    def get_latest_xml(self):

        if self.__ods_xml_data is None:
            data_filename = self.__retrieve_latest_datafile()
            self.__ods_xml_data = self.__import_latest_datafile(data_filename)
        else:
            return __ods_xml_data
