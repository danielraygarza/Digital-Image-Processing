class interpolation:

    def linear_interpolation(self, Pt1, Pt2, x):
        """Computes the linear interpolation value at some iD location x between two 1D points (Pt1 and Pt2).
        
        There are no arguments defined in the function definition on purpose. It is left upto the student to define any requierd arguments.
        Please change the signature of the function and add the arguments based on your implementation.
        
        The function ideally takes two 1D points Pt1 and Pt2, and their intensitites I(Pt1), I(Pt2).
        return the interpolated intensity value (I(x)) at location x """

        # Write your code for linear interpolation here
        return Pt1 * (1-x) + Pt2 * x
    

    def bilinear_interpolation(self, img, point):
        """Computes the bilinear interpolation value at some 2D location x between four 2D points (Pt1, Pt2, Pt3, and Pt4).
        
        There are no arguments defined in the function definition on purpose. It is left upto the student to define any requierd arguments.
        Please change the signature of the function and add the arguments based on your implementation.
        
        The function ideally takes four 2D points Pt1, Pt2, Pt3, and Pt4, and their intensitites I(Pt1), I(Pt2), I(Pt3), and I(Pt4).
        return the interpolated intensity value (I(x)) at location x """

        # Write your code for bilinear interpolation here
        # Recall that bilinear interpolation performs linear interpolation three times
        # Please reuse or call linear interpolation method three times by passing the appropriate parameters to compute this task

        # get dimensions of input image
        height = img.shape[0]
        width = img.shape[1]
        x, y = point # get x and y coordinates of the desired point

        # get coordinates of the four surrounding points
        Pt1 = int(x)
        Pt2 = int(y)
        Pt3 = Pt1 + 1
        Pt4 = Pt2 + 1

        # get intensity values at the four points
        I_Pt1 = img[max(Pt2, 0), max(Pt1, 0)]
        I_Pt2 = img[max(Pt2, 0), min(Pt3, width - 1)]
        I_Pt3 = img[min(Pt4, height - 1), max(Pt1, 0)]
        I_Pt4 = img[min(Pt4, height - 1), min(Pt3, width - 1)]
        
        # call interpolation 3 times
        # linear interpolation in the x direction
        I_inter1 = self.linear_interpolation(I_Pt1, I_Pt2, x - Pt1)
        I_inter2 = self.linear_interpolation(I_Pt3, I_Pt4, x - Pt1)
        
        # linear interpolation in the y direction
        I_x = self.linear_interpolation(I_inter1, I_inter2, y - Pt2)

        return I_x