
# Load XML
import xml.etree.ElementTree as ET
tree = ET.parse('example003_full.xml')
root = tree.getroot()

# Iterate through records (in the case of VRA Core 4.0 they must contain at least one attribute with its respective ID)
for count_records, record in enumerate(root, start=1):

    # Print counter number and name of record
    print('\n{} {} ({}): '.format('Record', count_records, record.tag.replace('{http://www.vraweb.org/vracore4.htm}', '')), end='')
    # Print only the first two attribute-value pairs of the record
    count_attributes_record = 0
    for attribute, value in record.attrib.items():
        count_attributes_record += 1
        if count_attributes_record == 2 or len(record.attrib) == 1:
            print('{} - {}'.format(attribute, value))
            break
        else:
            print('{} - {}, '.format(attribute, value), end='')

    # Iterate through elementsets
    for count_elementsets, elementset in enumerate(record, start=1):

        # Skip elementsets without attributes
        if elementset.attrib != {}:

            # Print counter number and name of elementset
            print('{} {} ({}): '.format('Elementset', count_elementsets, elementset.tag.replace('{http://www.vraweb.org/vracore4.htm}', '')), end='')
            # Print only the first two attribute-value pairs of the elementset
            count_attributes_elementsets = 0
            for attribute, value in elementset.attrib.items():
                count_attributes_elementsets += 1
                if count_attributes_elementsets == 2 or len(elementset.attrib) == 1:
                    print('{} - {}'.format(attribute, value))
                    break
                else:
                    print('{} - {}, '.format(attribute, value), end='')

        # Iterate through elements
        for count_elements, element in enumerate(elementset, start=1):
            # Skip elements without attributes
            if element.attrib != {}:
                # First print counter number and name of parent elementset to avoid confusion
                print('{} {} ({}) '.format('Elementset', count_elementsets, elementset.tag.replace('{http://www.vraweb.org/vracore4.htm}', '')), end='')
                # Print counter number and name of element
                print('{} {} ({}): '.format('Element', count_elements, element.tag.replace('{http://www.vraweb.org/vracore4.htm}', '')), end='')
                # Print only the first two attribute-value pairs of the element
                count_attributes_elements = 0
                for attribute, value in element.attrib.items():
                    count_attributes_elements += 1
                    if count_attributes_elements == 2 or len(element.attrib) == 1:
                        print('{} - {}'.format(attribute, value))
                        break
                    else:
                        print('{} - {}, '.format(attribute, value), end='')

            # Iterate through subelements
            for count_subelements, subelement in enumerate(element, start=1):
                # Skip subelements without attributes
                if subelement.attrib != {}:
                    # First print counter number and name of parent elementset to avoid confusion
                    print('{} {} ({}) '.format('Elementset', count_elementsets, elementset.tag.replace('{http://www.vraweb.org/vracore4.htm}', '')), end='')
                    # Second print counter number and name of parent element to avoid confusion
                    print('{} {} ({}) '.format('Element', count_elements, element.tag.replace('{http://www.vraweb.org/vracore4.htm}', '')), end='')
                    # Print counter number and name of subelement
                    print('{} {} ({}): '.format('Subelement', count_subelements, subelement.tag.replace('{http://www.vraweb.org/vracore4.htm}', '')), end='')
                    # Print only the first two attribute-value pairs of the subelement
                    count_attributes_subelements = 0
                    for attribute, value in subelement.attrib.items():
                        count_attributes_subelements += 1
                        if count_attributes_subelements == 2 or len(subelement.attrib) == 1:
                            print('{} - {}'.format(attribute, value))
                            break
                        else:
                            print('{} - {}, '.format(attribute, value), end='')
