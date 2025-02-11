# tampermonkey-from-local
Give TamperMonkey access to a directory on your local machine.
Scripts can be edited and version-controlled locally, in that directory.
And they can be updated in TamperMonkey though the usual graphical interface.

This script automatizes the steps of [this tutorial](https://gist.github.com/DerDemystifier/2950519cbbdfefc900614384a57433c4) for a Linux system.

## Requirements

Python needs to be installed.
The script itself should work regardless of the Linux distribution.

## Installation

- Install Python if needed.
- In a terminal go to desired installation directory.
- Run
```
git clone https://github.com/stephane-coulomb/tampermonkey-from-local.git
cd tampermonkey-from-local
chmod u+x ./install.sh
./install.sh
```

## Usage

Run
```
./.venv/bin/python ./start_update_server.py
```
TamperMonkey (in fact, any application running on your machine) now has access to the contents of `./scripts` at `localhost:5008`.

### To install in TamperMonkey a script in `./scripts`

To install the example `./scripts/myscript.user.js`, either
- In your web browser, enter the `localhost:5008/myscript.user.js` URL. I suppose that may not work depending on your configuration (I don't know how/why `.js` files are associated to TamperMonkey on my system...)
- Or, equivalently, go to `localhost:5008` and click on the script you want to install .
- **OR** Create a new userscript from TamperMonkey's interface and copy/paste the code from `myscript.user.js`

### To update an installed script

- Update the version number in `./myscript.user.js`.
- From TamperMonkey's interface check for update.
