from .. import BaseALObject
from ..componentclass import ComponentClass


class DistributionClass(ComponentClass):

    defining_attributes = ('name', '_parameters', 'distribution')

    def __init__(self, name, distribution, parameters=None):
        super(DistributionClass, self).__init__(name, parameters)
        self.distribution = distribution

    def accept_visitor(self, visitor, **kwargs):
        """ |VISITATION| """
        return visitor.visit_componentclass(self, **kwargs)


class Distribution(BaseALObject):

    defining_attributes = ()

    def accept_visitor(self, visitor, **kwargs):
        """ |VISITATION| """
        return visitor.visit_distribution(self, **kwargs)