class QuickFindUF:
    """
    Quick-Find implementation of the Union-Find data structure.
    This is an eager algorithm.

    Attributes:
        components (list): A list where each index represents an element, and the value at that index represents its component.
        connected_components_count (int): The number of connected components.
        size (int): The total number of elements.
    """

    def __init__(self, N):
        """
        Initialize the Union-Find structure.

        Args:
            N (int): The number of elements.
        """
        self.components = list(range(N))
        self.connected_components_count = N
        self.size = N

    def _validate(self, p):
        """
        Validate if the index p is within the valid range.

        Args:
            p (int): The index to validate.
        """
        if p < 0 or p >= self.size:
            raise IndexError(
                f"Index {p} is out of bounds for QuickFindUF of size {self.size}"
            )

    def connected(self, p, q):
        """
        Check if elements p and q are connected.

        Args:
            p (int): The first element.
            q (int): The second element.

        Returns:
            bool: True if p and q are connected, otherwise False.
        """
        self._validate(p)
        self._validate(q)
        if p == q:
            return True  # Already connected (no need to check further)
        return self.components[p] == self.components[q]

    def get_connected_components_count(self):
        """
        Get the current number of connected components.

        Returns:
            int: The number of connected components.
        """
        return self.connected_components_count

    def union(self, p, q):
        """
        Perform the union of elements p and q.

        Args:
            p (int): The first element.
            q (int): The second element.
        """
        self._validate(p)
        self._validate(q)

        p_id = self.components[p]
        q_id = self.components[q]

        if p_id == q_id:
            return  # They are already connected.

        self.connected_components_count -= 1

        for i in range(self.size):
            if self.components[i] == p_id:
                self.components[i] = q_id
