# spatial-growth
## How to obtain the raw data
The file **curves_raw.npy** can be obtained from [this repository](https://github.com/Scan-o-Matic/scanomatic/wiki/Example-experimental-data).
Navigate through _Browse the contents_, and then to the _analysis/_ folder.
Download the **curves_raw.npy** file to the base of your clone of this repository.

## What order to run the notebooks
After cloning this repository, start by obtaining the **curves_raw.npy** file as described above.
Then run the **create_folders.sh** script `./create_folders.sh` from this folder.

Once the preparations are done, the general way is :
* First run the computation notebooks (level-?_\*.ipynb)
* Then run the figure notebooks (figure-*.ipynb)

Note that you need to run the **level-2_initial-alphas.ipynb** before any level-2\_*.ipynb and level-3_\*.ipynb notebook.

An additional dependency is for the **level-2\_alpha-epsilon\_k-phi.ipynb** notebook, which depends on **level-2\_alpha-epsilon\_k.ipynb** prior creating initial epsilon parameters.

## Synthetic branch
As the format of the original Scan-o-Matic data and our synthetic data changes slightly, it has been chosen to create a separate branch containing notebooks specially suited to that data.
Change the branch of your repository in order to run these notebooks.
