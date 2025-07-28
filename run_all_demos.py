#!/usr/bin/env python3
"""
Comprehensive Algorithm and Data Structure Demo Runner

This script runs demonstrations of all implemented algorithms and data structures
with an interactive menu system for easy navigation and learning.

Execute with: python run_all_demos.py

Author: Algorithm Learning Repository
"""

import os
import sys
import time
import importlib.util


class AlgorithmDemoRunner:
    """Main demo runner for all algorithms and data structures."""
    
    def __init__(self):
        """Initialize the demo runner."""
        self.modules = {
            "Array Operations": "data_structures/arrays/array_operations.py",
            "Linked Lists": "data_structures/linked_lists/linked_list_implementation.py",
            "Stacks": "data_structures/stacks/stack_implementation.py", 
            "Queues": "data_structures/queues/queue_implementation.py",
            "Binary Trees": "data_structures/trees/binary_tree_implementation.py",
            "Sorting Algorithms": "algorithms/sorting/sorting_algorithms.py",
            "Search Algorithms": "algorithms/searching/search_algorithms.py",
            "Dynamic Programming": "algorithms/dynamic_programming/dp_algorithms.py",
        }
        
        self.descriptions = {
            "Array Operations": "Dynamic arrays, common operations, and array-based algorithms",
            "Linked Lists": "Singly, doubly, and circular linked lists with operations", 
            "Stacks": "LIFO data structure with array and linked list implementations",
            "Queues": "FIFO data structure including circular, priority, and deque",
            "Binary Trees": "Binary trees, BST, AVL trees with traversals and operations",
            "Sorting Algorithms": "Comprehensive sorting algorithms with complexity analysis",
            "Search Algorithms": "Linear, binary, advanced searches, and graph traversal",
            "Dynamic Programming": "Classic DP problems with memoization and tabulation",
        }
    
    def clear_screen(self):
        """Clear the terminal screen."""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def print_header(self):
        """Print the main header."""
        print("🚀" + "=" * 78 + "🚀")
        print(" " * 20 + "COMPREHENSIVE ALGORITHMS & DATA STRUCTURES")
        print(" " * 30 + "Interactive Demo Runner")
        print("🚀" + "=" * 78 + "🚀")
        print()
    
    def print_menu(self):
        """Print the main menu."""
        print("📚 Available Demonstrations:")
        print("-" * 50)
        
        for i, (name, _) in enumerate(self.modules.items(), 1):
            description = self.descriptions.get(name, "")
            print(f"{i:2d}. {name:<20} - {description}")
        
        print(f"{len(self.modules) + 1:2d}. {'Run All Demos':<20} - Execute all demonstrations")
        print(f"{len(self.modules) + 2:2d}. {'Exit':<20} - Quit the program")
        print("-" * 50)
    
    def load_and_run_module(self, module_path: str, module_name: str):
        """Load and run a specific module."""
        try:
            # Get the full path
            full_path = os.path.abspath(module_path)
            
            if not os.path.exists(full_path):
                print(f"❌ Error: Module file not found: {full_path}")
                return False
            
            # Load the module
            spec = importlib.util.spec_from_file_location(module_name, full_path)
            module = importlib.util.module_from_spec(spec)
            
            # Add the module directory to sys.path temporarily
            module_dir = os.path.dirname(full_path)
            if module_dir not in sys.path:
                sys.path.insert(0, module_dir)
            
            # Execute the module
            print(f"🎯 Loading {module_name}...")
            print("=" * 80)
            
            spec.loader.exec_module(module)
            
            # Remove the added path
            if module_dir in sys.path:
                sys.path.remove(module_dir)
            
            return True
            
        except Exception as e:
            print(f"❌ Error running {module_name}: {str(e)}")
            return False
    
    def run_single_demo(self, choice: int):
        """Run a single demonstration."""
        if choice < 1 or choice > len(self.modules):
            print("❌ Invalid choice!")
            return
        
        module_names = list(self.modules.keys())
        module_name = module_names[choice - 1]
        module_path = self.modules[module_name]
        
        self.clear_screen()
        print(f"🎯 Running: {module_name}")
        print("=" * 80)
        print()
        
        success = self.load_and_run_module(module_path, module_name.lower().replace(" ", "_"))
        
        if success:
            print("\n" + "=" * 80)
            print(f"✅ {module_name} demonstration completed!")
        else:
            print(f"❌ Failed to run {module_name} demonstration!")
        
        self.pause_for_user()
    
    def run_all_demos(self):
        """Run all demonstrations in sequence."""
        self.clear_screen()
        print("🚀 Running All Demonstrations")
        print("=" * 80)
        print()
        
        total_modules = len(self.modules)
        successful = 0
        
        for i, (module_name, module_path) in enumerate(self.modules.items(), 1):
            print(f"\n🎯 [{i}/{total_modules}] Running: {module_name}")
            print("-" * 60)
            
            success = self.load_and_run_module(module_path, module_name.lower().replace(" ", "_"))
            
            if success:
                successful += 1
                print(f"✅ {module_name} completed successfully!")
            else:
                print(f"❌ {module_name} failed!")
            
            if i < total_modules:
                print("\n" + "⏳ Waiting 3 seconds before next demo...")
                time.sleep(3)
        
        print("\n" + "=" * 80)
        print(f"🏁 All Demonstrations Complete!")
        print(f"✅ Successful: {successful}/{total_modules}")
        
        if successful < total_modules:
            print(f"❌ Failed: {total_modules - successful}/{total_modules}")
        
        self.pause_for_user()
    
    def pause_for_user(self):
        """Pause and wait for user input."""
        print("\n" + "=" * 80)
        try:
            input("Press Enter to continue...")
        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            sys.exit(0)
    
    def show_module_info(self):
        """Show information about all modules."""
        self.clear_screen()
        print("📖 Module Information")
        print("=" * 80)
        print()
        
        for module_name, module_path in self.modules.items():
            print(f"📁 {module_name}")
            print(f"   📄 File: {module_path}")
            print(f"   📝 Description: {self.descriptions.get(module_name, 'No description')}")
            print(f"   📊 Status: {'✅ Available' if os.path.exists(module_path) else '❌ Missing'}")
            print()
        
        self.pause_for_user()
    
    def run(self):
        """Main run loop."""
        while True:
            try:
                self.clear_screen()
                self.print_header()
                self.print_menu()
                
                print()
                choice = input("🎯 Enter your choice (1-{}): ".format(len(self.modules) + 2))
                
                if not choice.isdigit():
                    print("❌ Please enter a valid number!")
                    time.sleep(1)
                    continue
                
                choice = int(choice)
                
                if choice == len(self.modules) + 1:  # Run all demos
                    self.run_all_demos()
                elif choice == len(self.modules) + 2:  # Exit
                    self.clear_screen()
                    print("👋 Thank you for exploring algorithms and data structures!")
                    print("🎓 Keep learning and coding!")
                    break
                elif 1 <= choice <= len(self.modules):
                    self.run_single_demo(choice)
                else:
                    print("❌ Invalid choice! Please try again.")
                    time.sleep(1)
                    
            except KeyboardInterrupt:
                self.clear_screen()
                print("\n👋 Goodbye! Thanks for learning with us!")
                break
            except Exception as e:
                print(f"❌ An error occurred: {str(e)}")
                self.pause_for_user()


def check_dependencies():
    """Check if all required files exist."""
    runner = AlgorithmDemoRunner()
    missing_files = []
    
    for module_name, module_path in runner.modules.items():
        if not os.path.exists(module_path):
            missing_files.append((module_name, module_path))
    
    if missing_files:
        print("⚠️  Warning: Some module files are missing:")
        for module_name, module_path in missing_files:
            print(f"   ❌ {module_name}: {module_path}")
        print()
        print("🔧 You can still run available modules.")
        return False
    
    return True


def show_welcome_message():
    """Show welcome message and instructions."""
    print("🎓" + "=" * 78 + "🎓")
    print(" " * 25 + "WELCOME TO THE ALGORITHM TUTORIAL!")
    print("🎓" + "=" * 78 + "🎓")
    print()
    print("📚 This comprehensive tutorial covers:")
    print("   • Data Structures: Arrays, Linked Lists, Stacks, Queues, Trees")
    print("   • Algorithms: Sorting, Dynamic Programming, and more")
    print("   • Detailed explanations with time/space complexity analysis")
    print("   • Multiple implementation approaches and optimizations")
    print()
    print("🎯 Each demonstration includes:")
    print("   • Step-by-step algorithm execution")
    print("   • Real-world examples and use cases")
    print("   • Performance comparisons")
    print("   • Best practices and insights")
    print()
    print("🚀 Ready to start learning? Let's dive in!")
    print("=" * 80)
    print()
    
    try:
        input("Press Enter to continue...")
    except KeyboardInterrupt:
        print("\n👋 Goodbye!")
        sys.exit(0)


if __name__ == "__main__":
    # Clear screen and show welcome
    os.system('cls' if os.name == 'nt' else 'clear')
    show_welcome_message()
    
    # Check dependencies
    os.system('cls' if os.name == 'nt' else 'clear')
    print("🔍 Checking module availability...")
    all_available = check_dependencies()
    
    if all_available:
        print("✅ All modules are available!")
    
    time.sleep(2)
    
    # Run the demo runner
    runner = AlgorithmDemoRunner()
    runner.run()