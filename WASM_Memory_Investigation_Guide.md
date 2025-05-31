# WASM Game Memory Investigation Guide

## 🎯 Goal
Extract score values from a WebAssembly (WASM) game running in a browser by reading memory addresses.

## 📋 Prerequisites

### Software Requirements
- **Chrome Browser** (latest version with WASM debugging support)
- **Python 3.7+** with packages:
  ```bash
  pip install selenium pyautogui psutil
  ```
- **ChromeDriver** (automatically managed by Selenium)

### Optional Tools
- **C/C++ DevTools Support (DWARF) Extension** for advanced WASM debugging
- **Memory analysis tools** like Cheat Engine (for comparison)

## 🔍 Investigation Methods

### Method 1: Chrome DevTools Memory Inspector (Recommended)

This is the most reliable and user-friendly approach.

#### Step-by-Step Process:

1. **Open the Game**
   - Navigate to your WASM game in Chrome
   - Ensure the game is fully loaded

2. **Open DevTools**
   - Press `F12` or `Ctrl+Shift+I`
   - Go to the **Sources** tab

3. **Find WASM Files**
   - Look for `.wasm` files in the file tree
   - These contain the compiled WebAssembly code

4. **Set Breakpoints**
   - Click on line numbers in the WASM disassembly to set breakpoints
   - Alternatively, use the **Pause on exceptions** feature

5. **Trigger Execution**
   - Play the game to trigger the breakpoint
   - The debugger will pause execution

6. **Access Memory Inspector**
   - In the **Scope** panel (right side), look for:
     - `env.memory`
     - `WebAssembly.Memory`
     - Memory-related objects
   - Right-click on memory object → **"Reveal in Memory Inspector panel"**

7. **Find Your Score**
   - Change your game score to a recognizable value (e.g., 12345)
   - In Memory Inspector, navigate through memory addresses
   - Look for your score value in different formats:
     - **Decimal**: Direct number representation
     - **Hexadecimal**: Base-16 representation
     - **ASCII**: Text representation (if applicable)

8. **Note the Address**
   - When you find your score, note the memory address (e.g., `0x00001234`)
   - This address will be used for continuous monitoring

#### Memory Inspector Features:
- **Address Navigation**: Jump to specific memory addresses
- **Data Format Toggle**: View as integers, floats, bytes
- **Endianness Control**: Switch between big-endian and little-endian
- **Search Functionality**: Search for specific values

### Method 2: JavaScript Memory Access

This method uses JavaScript injection to programmatically access WASM memory.

#### How It Works:
1. **Inject JavaScript** into the game page
2. **Find WASM Instances** by scanning global objects
3. **Access Memory Buffer** through WebAssembly.Memory
4. **Search for Values** using typed arrays (Int32Array, Float32Array)

#### Code Example:
```javascript
// Find WASM instances
function findWasmInstances() {
    const instances = [];
    for (let key in window) {
        try {
            if (window[key] && window[key].exports && window[key].exports.memory) {
                instances.push({
                    name: key,
                    memory: window[key].exports.memory,
                    instance: window[key]
                });
            }
        } catch (e) {
            // Ignore access errors
        }
    }
    return instances;
}

// Search for a specific value
function searchMemoryForValue(memory, targetValue) {
    const view = new Int32Array(memory.buffer);
    const results = [];
    
    for (let i = 0; i < view.length; i++) {
        if (view[i] === targetValue) {
            results.push({
                address: i * 4,
                value: view[i]
            });
        }
    }
    return results;
}
```

### Method 3: Pattern Analysis

When you can't find the exact score value, analyze memory patterns.

#### Process:
1. **Take Memory Snapshots** at different score values
2. **Compare Changes** between snapshots
3. **Identify Patterns** (increasing values, consistent locations)
4. **Filter Candidates** based on typical score characteristics

#### What to Look For:
- **Increasing Values**: Scores typically increase over time
- **Reasonable Ranges**: Scores are usually within expected bounds
- **Consistent Locations**: Score addresses don't change frequently
- **Data Type Patterns**: Scores are often integers or floats

### Method 4: Continuous Monitoring

Once you've found the score address, monitor it continuously.

#### Implementation:
```python
def monitor_score(driver, memory_address):
    while True:
        score = driver.execute_script(f"""
            const wasmInstances = findWasmInstances();
            if (wasmInstances.length > 0) {{
                const memory = wasmInstances[0].memory;
                const view = new Int32Array(memory.buffer);
                return view[{memory_address} / 4];
            }}
            return null;
        """)
        
        print(f"Current Score: {score}")
        time.sleep(1)
```

## 🛠️ Troubleshooting Common Issues

### Issue 1: No WASM Memory Found
**Symptoms**: JavaScript can't find WebAssembly instances
**Solutions**:
- Check if the game actually uses WebAssembly
- Look for different memory access patterns
- Try accessing memory through different global objects

### Issue 2: Memory Access Denied
**Symptoms**: JavaScript throws security errors
**Solutions**:
- Ensure you're running on the same origin
- Check for Content Security Policy restrictions
- Try using browser extensions for elevated access

### Issue 3: Score Value Not Found
**Symptoms**: Memory search returns no results
**Solutions**:
- Try different data types (int32, float32, int16)
- Search for encoded or transformed values
- Look for the score in different number bases
- Consider that the score might be stored as a string

### Issue 4: Address Changes Between Sessions
**Symptoms**: Previously found addresses no longer work
**Solutions**:
- WASM memory layout can change between loads
- Use pattern analysis to find the new address
- Look for relative offsets from known structures

## 📊 Data Types and Formats

### Common Score Storage Formats:
- **32-bit Integer** (`Int32Array`): Most common for integer scores
- **32-bit Float** (`Float32Array`): For scores with decimal places
- **16-bit Integer** (`Int16Array`): For smaller score ranges
- **64-bit Integer** (`BigInt64Array`): For very large scores

### Memory Layout Considerations:
- **Endianness**: Little-endian vs big-endian byte order
- **Alignment**: Values might be aligned to 4-byte or 8-byte boundaries
- **Padding**: Extra bytes between data structures

## 🔒 Security and Ethical Considerations

### Legal Considerations:
- Only analyze games you own or have permission to modify
- Respect terms of service and end-user license agreements
- Don't use this for cheating in online multiplayer games

### Technical Limitations:
- Some games use obfuscation or encryption
- Anti-cheat systems may detect memory analysis
- Browser security features may block access

## 🚀 Advanced Techniques

### 1. Memory Mapping
Create a map of the entire WASM memory space to understand data structures.

### 2. Reverse Engineering
Use tools like Ghidra or IDA Pro to analyze the WASM binary offline.

### 3. Dynamic Analysis
Monitor memory changes in real-time to understand game logic.

### 4. Pointer Following
If the score is stored via pointers, follow the pointer chain to find the actual value.

## 📝 Example Workflow

1. **Setup**: Run the Python script with your game URL
2. **Initial Discovery**: Use Method 1 (DevTools) to manually find the score
3. **Automation**: Use Method 2 (JavaScript) to programmatically access the score
4. **Monitoring**: Use Method 3 to continuously track score changes
5. **Integration**: Incorporate the score reading into your automation system

## 🎯 Success Indicators

You've successfully found the score when:
- ✅ The memory value matches your current game score
- ✅ The value updates when your score changes
- ✅ The address remains consistent during gameplay
- ✅ You can read the value programmatically

## 📚 Additional Resources

- [Chrome DevTools Memory Inspector Documentation](https://developer.chrome.com/docs/devtools/memory-inspector/)
- [WebAssembly Debugging Guide](https://developer.chrome.com/blog/wasm-debugging-2020)
- [MDN WebAssembly Documentation](https://developer.mozilla.org/en-US/docs/WebAssembly)
- [WASM Memory Model Specification](https://webassembly.github.io/spec/core/syntax/modules.html#memories)

## 🤝 Getting Help

If you encounter issues:
1. Check the browser console for error messages
2. Verify that the game actually uses WebAssembly
3. Try different data types and search patterns
4. Consider that some games use complex data structures
5. Ask for help with specific error messages or game details

Remember: This is a learning exercise in reverse engineering and memory analysis. Always respect software licenses and terms of service! 