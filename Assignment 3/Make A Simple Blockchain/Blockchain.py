import hashlib
import json

class Block:
    BlockNumber = 0
    BlockData = 0
    NextBlock = 0
    HashValue = 0
    PreviousHash = 0
    NonceValue = 0

    def __init__(self, BlockData):
        self.BlockData = BlockData

    def HashValue(self):
        HashFunc = hashlib.sha256()
        HashFunc.update(
            str(self.NonceValue).encode('utf-8') + str(self.BlockData).encode('utf-8') + str(self.PreviousHash).encode(
                'utf-8'))
        return HashFunc.hexdigest()

    def __str__(self):
        return " Block Number: " + str(self.BlockNumber) + "\n Block Hash: " + str(
            self.HashValue()) + "\n Hash of the Previous Block: " + str(self.PreviousHash) + "\n Nonce Value: " + str(
            self.NonceValue) + "\n----------------------------------------------------------------------------------------------------"

class Blockchain:
    Genesis_Block = json.loads((open('GenesisBlock.json')).read())
    TheBlock = Block(Genesis_Block)
    TheBlock.BlockNumber = 1
    dummy = head = TheBlock

    def Append(self, TheBlock):
        TheBlock.BlockNumber = self.TheBlock.BlockNumber + 1
        TheBlock.PreviousHash = self.TheBlock.HashValue()
        self.TheBlock.NextBlock = TheBlock
        self.TheBlock = self.TheBlock.NextBlock

    def Mining(self, TheBlock, Puzzle):
        TheBlock.PreviousHash = self.TheBlock.HashValue()
        while True:
            TempPuzzle = TheBlock.HashValue()
            TempPuzzle = str(TempPuzzle)
            if (TempPuzzle[-4:] == Puzzle):
                self.Append(TheBlock)
                break
            else:
                TheBlock.NonceValue = TheBlock.NonceValue + 1

Ledger_Num2 = json.loads((open('Ledger_Number2.json')).read())
Ledger_Num3 = json.loads((open('Ledger_Number3.json')).read())
Ledger_Num4 = json.loads((open('Ledger_Number4.json')).read())
Ledger_Num5 = json.loads((open('Ledger_Number5.json')).read())
Ledger_Num6 = json.loads((open('Ledger_Number6.json')).read())
Ledger_Num7 = json.loads((open('Ledger_Number7.json')).read())
Ledger_Num8 = json.loads((open('Ledger_Number8.json')).read())
Ledger_Num9 = json.loads((open('Ledger_Number9.json')).read())
Ledger_Num10 = json.loads((open('Ledger_Number10.json')).read())
Ledger_Num11 = json.loads((open('Ledger_Number11.json')).read())
Ledger_Num12 = json.loads((open('Ledger_Number12.json')).read())
Ledger_Num13 = json.loads((open('Ledger_Number13.json')).read())
Ledger_Num14 = json.loads((open('Ledger_Number14.json')).read())
Ledger_Num15 = json.loads((open('Ledger_Number15.json')).read())
Ledger_Num16 = json.loads((open('Ledger_Number16.json')).read())

Puzzle_Num2 = json.loads((open('Math_Problem_Number2.json')).read())
Math_Problem_Num2 = Puzzle_Num2["mathProblem"]
Puzzle_Num3 = json.loads((open('Math_Problem_Number3.json')).read())
Math_Problem_Num3 = Puzzle_Num3["mathProblem"]
Puzzle_Num4 = json.loads((open('Math_Problem_Number4.json')).read())
Math_Problem_Num4 = Puzzle_Num4["mathProblem"]
Puzzle_Num5 = json.loads((open('Math_Problem_Number5.json')).read())
Math_Problem_Num5 = Puzzle_Num5["mathProblem"]
Puzzle_Num6 = json.loads((open('Math_Problem_Number6.json')).read())
Math_Problem_Num6 = Puzzle_Num6["mathProblem"]
Puzzle_Num7 = json.loads((open('Math_Problem_Number7.json')).read())
Math_Problem_Num7 = Puzzle_Num7["mathProblem"]
Puzzle_Num8 = json.loads((open('Math_Problem_Number8.json')).read())
Math_Problem_Num8 = Puzzle_Num8["mathProblem"]
Puzzle_Num9 = json.loads((open('Math_Problem_Number9.json')).read())
Math_Problem_Num9 = Puzzle_Num9["mathProblem"]
Puzzle_Num10 = json.loads((open('Math_Problem_Number10.json')).read())
Math_Problem_Num10 = Puzzle_Num10["mathProblem"]
Puzzle_Num11 = json.loads((open('Math_Problem_Number11.json')).read())
Math_Problem_Num11 = Puzzle_Num11["mathProblem"]
Puzzle_Num12 = json.loads((open('Math_Problem_Number12.json')).read())
Math_Problem_Num12 = Puzzle_Num12["mathProblem"]
Puzzle_Num13 = json.loads((open('Math_Problem_Number13.json')).read())
Math_Problem_Num13 = Puzzle_Num13["mathProblem"]
Puzzle_Num14 = json.loads((open('Math_Problem_Number14.json')).read())
Math_Problem_Num14 = Puzzle_Num14["mathProblem"]
Puzzle_Num15 = json.loads((open('Math_Problem_Number15.json')).read())
Math_Problem_Num15 = Puzzle_Num15["mathProblem"]
Puzzle_Num16 = json.loads((open('Math_Problem_Number16.json')).read())
Math_Problem_Num16 = Puzzle_Num16["mathProblem"]

Simple_Blockchain = Blockchain()

Simple_Blockchain.Mining(Block(str(Ledger_Num2)), str(Math_Problem_Num2))
Simple_Blockchain.Mining(Block(str(Ledger_Num3)), str(Math_Problem_Num3))
Simple_Blockchain.Mining(Block(str(Ledger_Num4)), str(Math_Problem_Num4))
Simple_Blockchain.Mining(Block(str(Ledger_Num5)), str(Math_Problem_Num5))
Simple_Blockchain.Mining(Block(str(Ledger_Num6)), str(Math_Problem_Num6))
Simple_Blockchain.Mining(Block(str(Ledger_Num7)), str(Math_Problem_Num7))
Simple_Blockchain.Mining(Block(str(Ledger_Num8)), str(Math_Problem_Num8))
Simple_Blockchain.Mining(Block(str(Ledger_Num9)), str(Math_Problem_Num9))
Simple_Blockchain.Mining(Block(str(Ledger_Num10)), str(Math_Problem_Num10))
Simple_Blockchain.Mining(Block(str(Ledger_Num11)), str(Math_Problem_Num11))
Simple_Blockchain.Mining(Block(str(Ledger_Num12)), str(Math_Problem_Num12))
Simple_Blockchain.Mining(Block(str(Ledger_Num13)), str(Math_Problem_Num13))
Simple_Blockchain.Mining(Block(str(Ledger_Num14)), str(Math_Problem_Num14))
Simple_Blockchain.Mining(Block(str(Ledger_Num15)), str(Math_Problem_Num15))
#Simple_Blockchain.Mining(Block(str(Ledger_Num16)), str(Math_Problem_Num16))

while Simple_Blockchain.head != 0:
    print(Simple_Blockchain.head)
    Simple_Blockchain.head = Simple_Blockchain.head.NextBlock