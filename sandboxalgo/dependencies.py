# -*- coding: utf-8 -*-

__author__ = 'Sergey Sobko'

# The solution may be rewritten using graphs / trees


class CircularDependencies(Exception):
    pass


class DependencyTree(dict):
    """Dependency tree implementation.

    >>> DependencyTree({'a': [], 'b': []}).dependency_sequence
    ['a', 'b']

    >>> DependencyTree({ \
        'a': ['b', 'e'], \
        'b': ['c', 'd'], \
        'c': [], \
        'd': ['c', 'e'], \
        'e': ['c'], \
        'f': [] \
    }).dependency_sequence
    ['f', 'c', 'e', 'd', 'b']

    >>> DependencyTree({ \
        'a': ['b', 'c'], \
        'b': ['c', 'd'], \
        'c': [], \
        'd': ['a'] \
    }).dependency_sequence
    Traceback (most recent call last):
     ...
    CircularDependencies: ['a', 'b', 'd']
    """
    def _dependency_routes(self, start):
        dependency_routes = list()

        def dependency_route_inner(current, dependency_route=None):
            if dependency_route is None:
                dependency_route = [current]

            current_dependencies = self.get(current, [])
            if current_dependencies:
                for dependency in current_dependencies:
                    if dependency in dependency_route:
                        raise CircularDependencies(dependency_route)

                    dependency_routes.append(
                        dependency_route_inner(
                            dependency,
                            dependency_route + [dependency]
                        )
                    )

            return dependency_route

        dependency_route_inner(start)
        return dependency_routes

    def show_routes(self, current):
        for route in self._dependency_routes(current):
            print route

    @property
    def dependency_sequence(self):
        routes_dict = dict()
        end_routes = list()
        dependency_sequence_list = list()

        for start in self.iterkeys():
            dependency_routes = self._dependency_routes(start)

            if len(dependency_routes) == 0:
                end_routes.append(start)

            for route in dependency_routes:
                routes_dict.setdefault(len(route), []).append(route)

        for route_index in sorted(routes_dict, reverse=True):
            for route in routes_dict[route_index]:
                last_dependency = route[-1]
                if last_dependency not in dependency_sequence_list:
                    dependency_sequence_list.append(last_dependency)

        return filter(lambda d: d not in dependency_sequence_list,
                      end_routes) + dependency_sequence_list


if __name__ == '__main__':
    import doctest
    doctest.testmod()
