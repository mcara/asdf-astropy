from asdf.extension import Converter


class EquivalencyConverter(Converter):
    tags = ["tag:astropy.org:astropy/units/equivalency-*"]

    types = ["astropy.units.equivalencies.Equivalency"]

    def to_yaml_tree(self, obj, tag, ctx):
        return [
            {'name': name, 'kwargs_names': list(kw.keys()), 'kwargs_values': list(kw.values())}
            for name, kw in zip(obj.name, obj.kwargs)
        ]

    def from_yaml_tree(self, node, tag, ctx):
        from astropy.units import equivalencies

        components = []
        for equivalency_node in node:
            equivalency_method = getattr(equivalencies, equivalency_node["name"])
            kwargs = dict(zip(equivalency_node["kwargs_names"], equivalency_node["kwargs_values"]))
            components.append(equivalency_method(**kwargs))

        # The Equivalency class is a UserList that overrides __add__ to
        # provide special behavior when combined with another Equivalency.
        # We're using sum here to add each subsequent Equivalency to the
        # first so we end up with a single correctly combined Equivalency
        # object at the end.
        return sum(components[1:], components[0])
