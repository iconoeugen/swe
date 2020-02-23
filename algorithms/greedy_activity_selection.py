#!/usr/bin/python
"""Find the set with the maximum number of non-conflicting activities

Definition of non-conflicting two activities a and b:
    - a.start >= b.finish
    - b.start >= a.finish
"""

class Activity():
    """Activity

    Attributes:
        - activity -- activity name
        - start -- starting time of activity
        - end -- end time of activity
    """
    def __init__(self, activity : str, start : int, end : int):
        """Inits activity instance

        Arguments:
            activity {str} -- the activity name
            start {int} -- start time of activity
            end {int} -- end time of activity
        """
        self.activity = activity
        self.start = start
        self.end = end

class Activities():
    def __init__(self, activities = None):
        if activities == None:
            self.activities = []
        else:
            self.activities = activities

    def add(self, activity: Activity):
        self.activities.append(activity)

    def _select_earliest_after(self, after = None):
        """ Select activity that finishes at earliest
        from the remaining activities
        """
        earliest = None
        for a in self.activities:
            if after == None or a.start >= after:
                if earliest == None or earliest.end > a.end:
                    earliest = a

        return earliest

    def select_activities(self):
        # initialize solution
        solution = []

        # no activities
        if not self.activities:
            return solution

        n = len(self.activities)
        after = None
        # all activities can be part of solution, so we can have as many
        # elements in the solution as existing activities
        for i in range(n):
            earliest = self._select_earliest_after(after)

            # check feasibility of selected activity
            if not earliest:
                return solution
            solution.append(earliest)

            # make sure the search space is updated
            after = earliest.end

        return solution

    def select_activities_shortcut(self):
        """Same implementation using python implementation for sorting

        Returns:
            List[Activity] -- the optimal solution
        """
        solution = []

        if not self.activities:
            return solution

        self.activities.sort(key=lambda a : a.end)
        solution.append(self.activities[0])
        for a in self.activities[1:]:
            if solution[-1].end <= a.start:
                solution.append(a)

        return solution


if __name__ == "__main__":
    a1 = Activity("a1", 5 ,9)
    a2 = Activity("a2", 1 ,3)
    a3 = Activity("a3", 3 ,4)
    a4 = Activity("a4", 0 ,6)
    a5 = Activity("a5", 5 ,7)
    a6 = Activity("a6", 8 ,9)

    activities = Activities([a2, a1, a4, a5, a3, a6])

    solution = activities.select_activities()

    print("Solution = {}".format([a.activity for a in solution]))
    assert(solution == [a2, a3, a5, a6])