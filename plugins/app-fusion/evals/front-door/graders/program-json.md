---
type: regex
target: { source: file, path: analysis/work/program.json }
pattern: '"stack": "react-native"[\s\S]*"stack": "ios-native"|"stack": "ios-native"[\s\S]*"stack": "react-native"'
---

Both apps are linked with their detected stacks.
