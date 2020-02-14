Explain in detail the workings of a dynamic array:

- What is the runtime complexity to access an array, add or remove from the front, and add or remove from the back?
  The runtime complexity to access an array and adding or removing from the back are O(1) because adding or removing from the back does not require a shift whereas adding or removing from the front would be O(n) because you would need to shift the entire array over by one.
- What is the worse case scenario if you try to extend the storage size of a dynamic array?
  extending the storage can lead to doubling the array size which may extend the runtime complexity
  Explain how a blockchain is structured. What are the blocks, what is the chain? How is the data organized?
  blockchain is made of genisis block which are then followed by interconnedcted blocks which are all connected by hashes. this allows for security and transaction history.
  Explain how proof of work functions. How does it operate. How does this protect the chain from attack. What kind of attack is possible?
  proof of work adds computational work to create a new block in the chain. this protects the chain because in order to attack they would have to redo all of the proofs.
