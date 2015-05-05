from ...componentclass.utils import ComponentClassInterfaceInferer
from .visitors import RandomDistributionActionVisitor


class RandomDistributionClassInterfaceInferer(ComponentClassInterfaceInferer,
                                        RandomDistributionActionVisitor):

    """
    Not extended from base classes currently, just mixes in the randomdistribution-
    specific action visitor to the component-class interface inferer.
    """
    pass
