import numpy as np
from matplotlib import pyplot as plt

# Complete the following to make the plot
if __name__ == "__main__":
    data = np.load('sdss_galaxy_colors.npy')
    # Get a colour map
    cmap = plt.get_cmap('YlOrRd')

    # Define our colour indexes u-g and r-i
    x = data['u'] - data['g']
    y = data['r'] - data['i']

    # Make a redshift array
    redshift_arr = data['redshift']

    # Create the plot with plt.scatter and plt.colorbar
    plt.scatter(x, y, s=1, c=redshift_arr, lw =0, cmap = plt.get_cmap('YlOrRd'))
    plt.colorbar().set_label("redshift")
    
    # Define your axis labels and plot title
    plt.xlabel = "color index u-g"
    plt.ylabel = "color index r-i"
    plt.title = "Redshit(color) u-g vs r-i"

    # Set any axis limits
    plt.axis([-0.5,2.5,-0.5,1.0])

    plt.show()