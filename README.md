# Block Pruner

How would you go about deleting blocks of `[start;end]` if the block contains `615` in _example.txt_ ?

_example.txt_

```txt
a
2
start
a
b
615
b
d
end
f
a
g
start
610
h
i
end
b
3
start
e
e
615
s
s
end
a
```

```
$ block_pruner -i example.txt --start="start" --end="end" --needle="615"
a
2
f
a
g
start
610
h
i
end
b
3
a
```

## Development

For help getting started developing check [DEVELOPMENT.md](DEVELOPMENT.md)
