### **The L1 Norm (Manhattan Norm)**

∥v∥1=∑i=1n∣vi∣∥_v_∥1​=∑_i_=1_n_​∣_vi_​∣

The L1 norm sums the absolute values of all components. It is called the **Manhattan distance** because it measures the distance you would travel on a grid of city blocks - only horizontal and vertical moves are allowed, no diagonal shortcuts.

**ML Application - Lasso Regularization**: Adding λ∥w∥1_λ_∥_w_∥1​ to a loss function (L1 penalty) drives many weights to exactly zero, producing **sparse** models. This performs automatic feature selection: irrelevant features get weight 0 and are effectively removed. The sparsity arises because the L1 unit ball has corners at the axes, and the loss contours are likely to intersect these corners.


### **The L2 Norm (Euclidean Norm)**

∥v∥2=∑i=1nvi2∥_v_∥2​=∑_i_=1_n_​_vi_2​​

The L2 norm is the straight-line length of the vector - the most intuitive notion of "size." It corresponds to the Euclidean distance from the origin to the point v_v_ and is the default norm in most of linear algebra and machine learning.

**ML Application - Ridge Regularization**: Adding λ∥w∥22_λ_∥_w_∥22​ to a loss function (L2 penalty) shrinks all weights toward zero but rarely sets them exactly to zero. This reduces overfitting while keeping all features in the model. The L2 unit ball is a smooth hypersphere, so the loss contours generally intersect it at a point where all weights are small but non-zero.




### **The L-infinity Norm (Max Norm)**

∥v∥∞=max⁡i∣vi∣∥_v_∥∞​=max_i_​∣_vi_​∣

The L-infinity norm picks out the single largest absolute component. Geometrically, the unit ball under ∥⋅∥∞∥⋅∥∞​ is a hypercube (a square in 2D, a cube in 3D) rather than a sphere.

This corresponds to **Chebyshev distance**: on a chessboard, the minimum number of moves a king needs to travel between two squares. It is useful when you care about the worst-case deviation across all dimensions.