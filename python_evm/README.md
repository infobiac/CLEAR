# vython
---------
### A hopefully easy to use "transpiler" to build smart contracts in python
I say transpiler because technically it's targetting vyper, but because of all the great work the vyper team has done, this code will allow a direct Python -> EVM (or LLL) pipeline.
Functionally all this does is make available common evm types and builtins (specifically vyper builtins) to python through the use of dummy functions and variables. As such, only very light type checking happens prior to compilation (i.e. when constructing the contract). When the contract is compiled, it undergoes much more in depth type checking. I'd like to push checking to be more eager so errors can be found faster, but for now this is life. Also, numerous types are still missing. So far, this has only been constructed to allow the common "auction" example to be transpiled/compiled into EVM.
### Todos: 
* [ ] Add mappings
* [ ] Add arrays
* [ ] Finish all builtins
* [ ] Bubble up type checking