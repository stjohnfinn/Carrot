"""
Simple WASM Memory Reader
========================

A simplified example showing how to read memory from a WASM game.
This script demonstrates the core concepts without the full complexity.

Usage:
1. Run this script
2. Navigate to your WASM game
3. Follow the prompts to find and monitor your score

Requirements: pip install selenium
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

class SimpleMemoryReader:
    def __init__(self):
        self.driver = None
        self.setup_browser()
    
    def setup_browser(self):
        """Setup Chrome with WASM debugging enabled"""
        options = Options()
        options.add_argument("--enable-features=WebAssemblyDebugging")
        options.add_experimental_option("useAutomationExtension", False)
        
        self.driver = webdriver.Chrome(options=options)
        print("✅ Browser ready!")
    
    def find_wasm_memory(self):
        """Find WebAssembly memory instances"""
        js_code = """
        // Look for WASM instances in global scope
        function findWasmMemory() {
            const results = [];
            
            // Check common locations
            const locations = [
                'Module', 'wasmModule', 'instance', 'wasm',
                'game', 'engine', 'runtime'
            ];
            
            for (let loc of locations) {
                try {
                    if (window[loc] && window[loc].exports && window[loc].exports.memory) {
                        results.push({
                            name: loc,
                            memory: window[loc].exports.memory,
                            size: window[loc].exports.memory.buffer.byteLength
                        });
                    }
                } catch (e) {
                    // Ignore errors
                }
            }
            
            // Also check for direct memory objects
            for (let key in window) {
                try {
                    if (window[key] instanceof WebAssembly.Memory) {
                        results.push({
                            name: key,
                            memory: window[key],
                            size: window[key].buffer.byteLength
                        });
                    }
                } catch (e) {
                    // Ignore errors
                }
            }
            
            return results;
        }
        
        return findWasmMemory();
        """
        
        try:
            results = self.driver.execute_script(js_code)
            return results
        except Exception as e:
            print(f"Error finding WASM memory: {e}")
            return []
    
    def search_for_value(self, target_value, data_type='int32'):
        """Search for a specific value in WASM memory"""
        search_js = f"""
        function searchMemory(targetValue, dataType) {{
            const memories = findWasmMemory();
            const allResults = [];
            
            for (let mem of memories) {{
                const results = [];
                
                if (dataType === 'int32') {{
                    const view = new Int32Array(mem.memory.buffer);
                    for (let i = 0; i < view.length; i++) {{
                        if (view[i] === targetValue) {{
                            results.push({{
                                address: i * 4,
                                value: view[i],
                                memoryName: mem.name
                            }});
                        }}
                    }}
                }} else if (dataType === 'float32') {{
                    const view = new Float32Array(mem.memory.buffer);
                    for (let i = 0; i < view.length; i++) {{
                        if (Math.abs(view[i] - targetValue) < 0.001) {{
                            results.push({{
                                address: i * 4,
                                value: view[i],
                                memoryName: mem.name
                            }});
                        }}
                    }}
                }}
                
                allResults.push(...results);
            }}
            
            return allResults;
        }}
        
        // Add the findWasmMemory function
        {self.get_find_memory_function()}
        
        return searchMemory({target_value}, '{data_type}');
        """
        
        try:
            results = self.driver.execute_script(search_js)
            return results
        except Exception as e:
            print(f"Error searching memory: {e}")
            return []
    
    def read_memory_address(self, address, data_type='int32'):
        """Read a specific memory address"""
        read_js = f"""
        function readAddress(address, dataType) {{
            const memories = findWasmMemory();
            
            for (let mem of memories) {{
                try {{
                    if (dataType === 'int32') {{
                        const view = new Int32Array(mem.memory.buffer);
                        return view[address / 4];
                    }} else if (dataType === 'float32') {{
                        const view = new Float32Array(mem.memory.buffer);
                        return view[address / 4];
                    }}
                }} catch (e) {{
                    continue;
                }}
            }}
            return null;
        }}
        
        {self.get_find_memory_function()}
        
        return readAddress({address}, '{data_type}');
        """
        
        try:
            value = self.driver.execute_script(read_js)
            return value
        except Exception as e:
            print(f"Error reading address: {e}")
            return None
    
    def get_find_memory_function(self):
        """Return the JavaScript function to find WASM memory"""
        return """
        function findWasmMemory() {
            const results = [];
            const locations = ['Module', 'wasmModule', 'instance', 'wasm', 'game', 'engine', 'runtime'];
            
            for (let loc of locations) {
                try {
                    if (window[loc] && window[loc].exports && window[loc].exports.memory) {
                        results.push({
                            name: loc,
                            memory: window[loc].exports.memory,
                            size: window[loc].exports.memory.buffer.byteLength
                        });
                    }
                } catch (e) {}
            }
            
            for (let key in window) {
                try {
                    if (window[key] instanceof WebAssembly.Memory) {
                        results.push({
                            name: key,
                            memory: window[key],
                            size: window[key].buffer.byteLength
                        });
                    }
                } catch (e) {}
            }
            
            return results;
        }
        """
    
    def interactive_session(self):
        """Run an interactive session to find and monitor scores"""
        print("\n🎮 Interactive WASM Memory Session")
        print("=" * 40)
        
        # Get game URL
        game_url = input("Enter your game URL: ").strip()
        if not game_url.startswith('http'):
            game_url = 'https://' + game_url
        
        print(f"🌐 Loading game: {game_url}")
        self.driver.get(game_url)
        
        input("⏸️  Load the game and press Enter when ready...")
        
        # Find WASM memory
        print("🔍 Looking for WASM memory...")
        memories = self.find_wasm_memory()
        
        if not memories:
            print("❌ No WASM memory found!")
            print("💡 Tips:")
            print("   - Make sure the game uses WebAssembly")
            print("   - Try playing the game first to load WASM modules")
            print("   - Check browser console for errors")
            return
        
        print(f"✅ Found {len(memories)} WASM memory instance(s):")
        for i, mem in enumerate(memories):
            size_mb = mem['size'] / (1024 * 1024)
            print(f"   {i+1}. {mem['name']}: {size_mb:.1f} MB")
        
        # Search for score
        while True:
            print("\n🎯 Score Search")
            current_score = input("Enter your current score (or 'quit' to exit): ").strip()
            
            if current_score.lower() == 'quit':
                break
            
            if not current_score.isdigit():
                print("❌ Please enter a numeric score")
                continue
            
            score_value = int(current_score)
            print(f"🔍 Searching for value: {score_value}")
            
            # Search as integer
            results = self.search_for_value(score_value, 'int32')
            
            if results:
                print(f"🎯 Found {len(results)} matches:")
                for i, result in enumerate(results[:10]):  # Show first 10
                    print(f"   {i+1}. Address: 0x{result['address']:08x} = {result['value']} ({result['memoryName']})")
                
                # Ask user to select an address for monitoring
                if len(results) == 1:
                    chosen_address = results[0]['address']
                    print(f"📍 Using address: 0x{chosen_address:08x}")
                else:
                    try:
                        choice = int(input(f"Select address (1-{min(len(results), 10)}): ")) - 1
                        chosen_address = results[choice]['address']
                    except (ValueError, IndexError):
                        print("❌ Invalid selection")
                        continue
                
                # Start monitoring
                print(f"\n🔄 Monitoring address 0x{chosen_address:08x}")
                print("   Change your score in the game to verify!")
                print("   Press Ctrl+C to stop monitoring")
                
                try:
                    while True:
                        value = self.read_memory_address(chosen_address, 'int32')
                        if value is not None:
                            print(f"📊 Score: {value}")
                        else:
                            print("❌ Could not read value")
                        time.sleep(1)
                except KeyboardInterrupt:
                    print("\n⏹️  Monitoring stopped")
                    break
            else:
                print("❌ No matches found")
                print("💡 Try:")
                print("   - Different score values")
                print("   - Playing the game more")
                print("   - Checking if score is stored as float")
    
    def cleanup(self):
        """Clean up resources"""
        if self.driver:
            self.driver.quit()

def main():
    """Main function"""
    print("🎮 Simple WASM Memory Reader")
    print("=" * 30)
    print("This tool helps you find and read score values from WASM games.")
    print()
    
    reader = SimpleMemoryReader()
    
    try:
        reader.interactive_session()
    except KeyboardInterrupt:
        print("\n⏹️  Session interrupted")
    except Exception as e:
        print(f"\n❌ Error: {e}")
    finally:
        reader.cleanup()
        print("\n👋 Goodbye!")

if __name__ == "__main__":
    main() 