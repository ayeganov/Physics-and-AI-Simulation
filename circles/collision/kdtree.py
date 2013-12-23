#!/usr/bin/env python
import logging
log = logging.getLogger(__name__)

class KDTree(object):

    class Node(object):

        def __init__(self, data, split_axis, left=None, right=None):
            self._data = data
            self._child = (left, right)
            self._split_axis = split_axis

        @property
        def left(self):
            return self._child[0]

        @left.setter
        def left(self, node):
            self._child = (node, self.right)

        @property
        def right(self):
            return self._child[1]

        @right.setter
        def right(self, node):
            self._child = (self.left, node)

        @property
        def split_value(self):
            return self._data[self.split_axis]

        @property
        def split_axis(self):
            return self._split_axis

        def __eq__(self, other):
            if other is None:
                return False

            if len(self._data) != len(other._data):
                return False

            for k in xrange(len(self._data)):
                if self._data[k] != other._data[k]:
                    return False

            return True
                
        def axis_value(self, axis):
            return self._data[axis]

        def __repr__(self):
            return {'data': self._data, 'left':self.left, 'right':self.right}

    def __init__(self, data, k):
        '''
        Initialize the tree object.
        @param data - a list of tuples containing the points located in space
                      to be searched.
        @param k - number of dimensions the data contains
        '''
        self._data = data
        self._k = k
        self._root = None
        self._build_tree(data)
        
    def _build_tree(self, data):
        '''
        Builds the tree by traversing the given data list.
        @param data - a list of points in k-dimensional space
        @return - a list of nodes making up the KDTree
        '''
        if data is None:
            return
        else:
            _ = [self.insert(p) for p in data]
        
    def insert(self, point):
        '''
            Inserts a data point into an appropriate position in the tree.
            @param point - a 'k' dimensional tuple.
        '''
        if len(point) != self._k:
            raise ValueError("Data points being inserted into the tree must contain data for %s dimensions." % self._k)

        if self._root is None:
            log.debug("Creating root: {point}".format(point=point))
            self._root = KDTree.Node(point, 0)
        else:
            self._insert(self._root, point, 0)

    def _insert(self, node, point, axis):
        '''
            The associate function to the public insert. It recurses the tree
            and finds the location for the data point.
            @param node - current node being checked against point
            @param point - new data point to be inserted into the tree
            @param axis - what axis of data should be used for comparison.
        '''
        log.debug("inserting {point} into node {node} axis={axis}".format(point=point, node=node._data, axis=axis))

        node_value = node.axis_value(axis)
        point_value = point[axis]

        log.debug("nove value {nval}, point value {pval}".format(nval=node_value, pval=point_value))

        if point_value < node_value:
            if node.left is None:

                log.debug("Creating node {p} on left of {data}".format(p=point, data=node._data))

                node.left = KDTree.Node(point, axis)
            else:
                self._insert(node.left, point, (axis + 1) % self._k)
        else:
            if node.right is None:

                log.debug("Creating node {p} on right of {data}".format(p=point, data=node._data))

                node.right = KDTree.Node(point, axis)
            else:
                self._insert(node.right, point, (axis + 1) % self._k)
        
def binary_search(array, imin, imax):
    # test if array is empty
    if (imax < imin):
      # set is empty, so return value showing not found
      return None
    else:
        # calculate midpoint to cut set in half
        imid = (imin + imax) / 2

        print array[imid]
        binary_search(array, imin, imid-1)
        binary_search(array, imid+1, imax)

if __name__ == "__main__":

    vals = ((1, 1), (1, 2), (2, 1), (2, 2))
    tree = KDTree(vals, 2)

