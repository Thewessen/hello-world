# Making pretty column printed tables in Python

For some of my projects I needed support for nested tables.
I'm still learning Python, so I decided to wrote a module myself.

There are better tested modules on the web:
- [PrettyTable](https://pypi.org/project/PrettyTable/ "PrettyTable at pypi.org")
- [columnize](https://pypi.org/project/columnize/ "columnize at pypi.prg")
- [tabulate](https://pypi.org/project/tabulate/ "tabulate at pypi.org")

But they can't do what this baby can do ; )
Look at this awesome print!
```
This column contains a table with       This column contains a copy of the left   
three columns each containing a table   column!                         
with three columns!                                                            
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
found1            | found2              found1             | found2            
==================+===================  ===================+===================
blk| f..| m..| w..| blk| f..| m..| h..  blk| f..| mean| w..| blk| f..| m..| h..
---+----+----+----| ---+----+----+----  ---+----+-----+----| ---+----+----+----
AB | 0  | 8  | \n | AB | 0  | 8  | \n   AB | 0  | 8.9 | \n | AB | 0  | 8  | \n 
   |    |    | \n |    |    |    | \n      |    |     | \n |    |    |    | \n 
   |    |    | \n |    |    |    | \n      |    |     | \n |    |    |    | \n 
   |    |    |    |    |    |    |         |    |     |    |    |    |    |    
CD | 1  | 8  | \n | CD | 1  | 8  | \n   CD | 1  | 8.3 | \n | CD | 1  | 8  | \n 
   |    |    | \n |    |    |    | \n      |    |     | \n |    |    |    | \n 
   |    |    | \n |    |    |    | \n      |    |     | \n |    |    |    | \n 
   |    |    |    |    |    |    |         |    |     |    |    |    |    |    
EF | 2  | 7  | \n | EF | 2  | 7  | \n   EF | 2  | 7.8 | \n | EF | 2  | 7  | \n 
   |    |    | \n |    |    |    | \n      |    |     | \n |    |    |    | \n 
   |    |    | \n |    |    |    | \n      |    |     | \n |    |    |    | \n 
   |    |    |    |    |    |    |         |    |     |    |    |    |    |    
GH | 3  | 7  | \n | GH | 3  | 7  | \n   GH | 3  | 7.2 | \n | GH | 3  | 7  | \n 
   |    |    | \n |    |    |    | \n      |    |     | \n |    |    |    | \n 
   |    |    | \n |    |    |    | \n      |    |     | \n |    |    |    | \n 
   |    |    |    |    |    |    |         |    |     |    |    |    |    |    
IJ | 4  | 6  | \n | IJ | 4  | 6  | \n   IJ | 4  | 6.7 | \n | IJ | 4  | 6  | \n 
   |    |    | \n |    |    |    | \n      |    |     | \n |    |    |    | \n 
   |    |    | \n |    |    |    | \n      |    |     | \n |    |    |    | \n 
   |    |    |    |    |    |    |         |    |     |    |    |    |    |    
\n is allowed     | the end...          \n is allowed      | the end...        
inside a cell!    |                     inside a cell!     |                   
```
### Goodies
+ Nested tables are allowed!
+ Newlines in a cell are allowed
+ Tries to break a long line into multiple lines before printing
+ Trunking also available for lists, floats, ints, and of coures tables!
+ Piping the output in terminal is possible, e.g. ... | head -10
+ Well documented.

### Usages
(Inspired by prettytable)
1. Create a new table object:
```mytable = Table()```
2. Add rows 
```mytable.add_row(['A', 'row', 'with', 'five', 'columns'])```
   and/or columns 
```mytable.add_column(head='column', data=['A', 'column', 'with', 'five', 'rows'])```
3. Add/replace heading:
```mytable.add_head(['This', 'table', 'looks', 'awesome'])```
4. Print the table:
```print(mytable)```

```
T..| ta..| looks| awe..|         |
---+-----+------+------+---------+-------
A  | row | with | five | columns | A
   |     |      |      |         | column
   |     |      |      |         | with
   |     |      |      |         | five
   |     |      |      |         | rows
```
Note: You can see the head isn't taken into account when calculating
the column_width for printing, see Notes.

### Module info
tables.Table()

Keyword arguments:

    rows        -- Number of initial rows (default 0)
    columns     -- Number of initial columns (default 0)
    fill        -- Empty cell fill (default '')
    max_width   -- Max width of the Table for printing (default None)
    col_sep     -- Seperator between columns (default '|')
    head_sep    -- Seperator for heading/table.
                   First char is the char at crossing of head_sep with
                   col_sep, second char is the fillchar (default '+-')
                   When one char is given, crosschar and fillchar are
                   the same.

Table object properties:

    fill    -- String of the default fill for empty cells.
    col_sep -- String of the column seperator used.
    head_sep-- String of the head/table seperator used.

methods:

    add_head(data=[], fill=None)
          Add a list of column headings to the table.
          data    -- List containing the headings
          fill    -- Empty heading fill for excesive columns.
                     Note: If none given, the Table fill param is used!
    
    add_row(data=[], fill=None)
        Add a list of row data to the table.
        data    -- List containing cell data.
        fill    -- The filling too use when creating more cells to fit
                   the Table size.
                   Note: If none given, the Table fill param is used!
    
    add_column(head=None, data=[], fill=None)
        Add a list of column data to the table.
        head    -- The table heading of this column.
        data    -- List containing cell data.
        fill    -- The filling too use when creating more cells to fit
                   the Table size.
                   Note: If none given, the Table fill param is used!
    
    get(row=None, column=None)
        Returns an instance of the Table containing the heading and
        Cell(s) from the Table.
        Note: If both row and column are ommited, return an instance of
        the Table.
        row     -- Integer or range of the corresponding row
                   (index start at 0)
        column  -- Integer or range of the corresponding column
                   (index start at 0)
    
    log(row=None, column=None)
        Prints the Cell, row or column.
        Same as print(Table.get(row, column))
        Note: If both row and column are ommited, prints the whole
        Table.
        row     -- Integer or range of the corresponding row
                   (starting at 0)
        column  -- Integer or range of the corresponding column
                   (starting at 0)
    
    nr_of_rows()
        Returns the numbers of rows in the Table as integer.
    
    nr_of_columns()
        Returns the numbers of columns in the Table as integer.

    set_max_width(i)
        Sets the max_width of the Table
        i       -- Integer of maxs width (in chars)

### ToDo
- Add insert_column and insert_row to insert between excisting columns or rows
- Add sort method?
- Cells containing functions, for calculating sum, product etc.. of range of
  Cells

### Notes
- When setting max_width Table tries too shrink largest column first,
  This isn't always desirable, especially with nested tables of different
  sizes.
- Head isn't taken into account when setting/calculating column width.
  Is this the desired behaviour?
- Nested tables side by side won't line row by row... This leaves room for
  discussion. At the end, it's a cell containing a table, not a splitted
  cell...
