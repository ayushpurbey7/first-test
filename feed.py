import yaml
import xml.etree.ElementTree as xmlt
with open('feed.yaml', 'r') as yamlfile:
    yamldata=yaml.safe_load(yamlfile)

    rss_element=xmlt.Element('rss', {'version':'2.0', 
        'xmlns:itunes':'http://www.itunes.com/dtds/podcast-1.0.dtd', 
        'xmlns:content':'http://purl.org/rss/1.0/modules/content/'})

channel_element=xmlt.SubElement(rss_element, 'channel')
link_prefix=yamldata['link']

xmlt.SubElement(channel_element,'title').text=yamldata['title']
xmlt.SubElement(channel_element,'format').text=yamldata['format']
xmlt.SubElement(channel_element,'subtitle').text=yamldata['subtitle']
xmlt.SubElement(channel_element,'itunes:author').text=yamldata['author']
xmlt.SubElement(channel_element,'description').text=yamldata['description']
xmlt.SubElement(channel_element,'itunes:image', {'href': link_prefix + yamldata['image']})
xmlt.SubElement(channel_element,'language').text=yamldata['language']
xmlt.SubElement(channel_element,'link').text=link_prefix

xmlt.SubElement(channel_element,'itunes:category', {'text': link_prefix + yamldata['category']})

for item in yamldata['item']:
    item_element=xmlt.SubElement(channel_element, 'item')
    xmlt.SubElement(item_element, 'title').text=item['title']
    xmlt.SubElement(item_element, 'itunes:author').text=yamldata['author']
    xmlt.SubElement(item_element, 'description').text=item['description']
    xmlt.SubElement(item_element, 'itunes:duration').text=item['duration']
    xmlt.SubElement(item_element, 'pubDate').text=item['published']
    xmlt.SubElement(item_element, 'title').text=item['title']

enclosure=xmlt.SubElement(item_element, 'enclosure', {
    'url':link_prefix+item['file'],
    'type':'audio/mpeg',
    'length':item['length']
})

output_tree=xmlt.ElementTree(rss_element)
output_tree.write('podcast.xml', encoding='UTF-8', xml_declaration=True)