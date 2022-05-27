# Assessment 2: Expression Binary Tree

## Fast Start

1. Make sure your shell's path is in ExpressionToTree
2. Run the python file

    ```shell
    python ./ExpressionToBinaryTree.py
    ```

3. You need to input your option in the shell

    ```text
    # 1 #
    ----------
    # Options
    Please input your option!
            input
            reload
            exit
    ----------
    Your OPTION:
    ```

4. If you input the option **input**, you need to input your expression in the shell

   ```text
    ----------
    # Tips
    Please input your expression!
    ----------
    Your INPUT:
   ```

5. If you input the option **reload**, you need to choose one history expression and type **yes**, and skip the line with type **no**

6. If you input the option **exit**, you will exit the execution.

## Fast Test

1. Make sure your shell's path is in ExpressionToTree
2. Run the python file

```shell
    python -m unittest ./ExpressionToBinaryTree_test.py
```

## File Structure

    ExpressionToTree
    │  Expression.txt
    │  ExpressionToBinaryTree.py
    │  ExpressionToBinaryTree_test.py
    │  README.md
    │
    ├─Expression
    │      Expression.py
    │      __init__.py
    │
    ├─Node
    │      Node.py
    │      __init__.py
    │
    └─Stack
            Stack.py
            __init__.py

## File Explain

- **Expression.txt** -- Is a txt file which save expressions' history.
- **ExpressionToBinaryTree.py** -- The main file of changing Expression to Binary Tree.
- **ExpressionToBinaryTree_test.py** --  The unittest of changing Expression to Binary Tree.
- **Expression.py** -- The class of Expression which can input expression and change it to Binary Tree.
- **Node.py** -- The class of Binary Tree's Node which save node's value, left node and right node.
- **Stack.py** -- The class of Stack which is a frist-in-last-out data stucture.