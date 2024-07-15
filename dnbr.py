import rasterio
import numpy as np
import argparse

def main(args):
    nbr1 = rasterio.open(args.prefire)
    nbr2 = rasterio.open(args.postfire)
    window = rasterio.windows.from_bounds(*nbr2.bounds, transform=nbr1.transform)
    
    n1 = nbr1.read(1, window=window, boundless=False)
    n2 = nbr2.read(1, window=window, boundless=False)
    dnbr = n1 - n2
    
    meta = nbr2.meta.copy()
    meta.update({
        'driver': 'GTiff',
        'dtype': 'float32',
        'nodata': None,  # Set this to an appropriate nodata value if needed
        'width': dnbr.shape[1],
        'height': dnbr.shape[0],
        'count': 1,  # We're writing a single band
    })
    with rasterio.open(args.out, 'w', **meta) as dst:
        dst.write(dnbr.astype(np.float32), 1)
    return

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--prefire', type=str, required=True)
    parser.add_argument('--postfire', type=str, required=True)
    parser.add_argument('--out', type=str, default='dnbr.tif')

    args = parser.parse_args()
    main(args)