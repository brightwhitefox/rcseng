"""Definition of the course content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

from PloneRCS.app import appMessageFactory as _
from PloneRCS.app.interfaces import Icourse
from PloneRCS.app.config import PROJECTNAME

courseSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

courseSchema['title'].storage = atapi.AnnotationStorage()
courseSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(courseSchema, moveDiscussion=False)


class course(base.ATCTContent):
    """Description of the Example Type"""
    implements(Icourse)

    meta_type = "course"
    schema = courseSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-

atapi.registerType(course, PROJECTNAME)
