import streamlit as st

# ============================================
# PAGE CONFIGURATION
# ============================================

st.set_page_config(
    page_title="Haiti Seoul Love Story",
    page_icon="💕",
    layout="wide"
)

# ============================================
# CUSTOM CSS
# ============================================

st.markdown("""
<style>
    .main-title {
        text-align: center;
        color: #ff1493;
        font-size: 3rem;
        margin-bottom: 0;
    }
    .ascii-art {
        font-family: 'Courier New', monospace;
        font-size: 0.8rem;
        line-height: 1.2;
        color: #ff69b4;
        text-align: center;
        white-space: pre;
    }
    .game-text {
        font-size: 1.2rem;
        text-align: center;
        margin: 20px 0;
    }
    .code-editor {
        background-color: #1e1e1e;
        border-radius: 8px;
        padding: 20px;
        font-family: 'Courier New', monospace;
        font-size: 0.9rem;
        color: #d4d4d4;
        max-height: 500px;
        overflow-y: auto;
    }
    .code-header {
        background-color: #2d2d2d;
        padding: 10px;
        border-radius: 8px 8px 0 0;
        color: #cccccc;
        font-family: 'Courier New', monospace;
    }
    .line-number {
        color: #858585;
        display: inline-block;
        width: 50px;
        min-width: 50px;
        text-align: left;
        margin-right: 20px;
        padding-right: 10px;
        border-right: 1px solid #3e3e3e;
        user-select: none;
    }
    .keyword {
        color: #569cd6;
    }
    .string {
        color: #ce9178;
    }
    .function {
        color: #dcdcaa;
    }
    .comment {
        color: #6a9955;
    }
    .win-message {
        background: linear-gradient(45deg, #ff1493, #ff69b4);
        padding: 30px;
        border-radius: 15px;
        text-align: center;
        color: white;
        font-size: 2rem;
        animation: pulse 2s infinite;
    }
    .game-over {
        background-color: #2d2d2d;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        color: #ff6b6b;
        font-size: 1.5rem;
    }
</style>
""", unsafe_allow_html=True)

# ============================================
# ORIGINAL PYTHON CODE (for display)
# ============================================

ORIGINAL_CODE = '''def main_game():
    while True:
        print(\'\'\'
*******************************************************************************
_   _    _    ___ _____ ___ 
| | | |  / \\  |_ _|_   _|_ _|
| |_| | / _ \\  | |  | |  | | 
|  _  |/ ___ \\ | |  | |  | | 
|_| |_/_/   \\_\\___| |_| |___|

 ____  _____ ___  _   _ _     
/ ___|| ____/ _ \\| | | | |    
\\___ \\|  _|| | | | | | | |    
 ___) | |__| |_| | |_| | |___ 
|____/|_____\\___/ \\___/|_____|

  ♥ LOVE STORY ♥
*******************************************************************************
\'\'\')
        print("Welcome to Haiti Seoul love story. ")
        print("Your mission is to start true love between Jeffandy and Ladi Seoul.")
        print("Please type your answers!")

        answer1 = input("\\nDoes Ladi turn left to patio or turn right to exit? \\n left or right? ").lower()
        if answer1 == "left":
            print("nice move! \\n")
            answer2 = input("Does Ladi walk to Jeffandy in corner or stand with friends? \\n walk or stand? ").lower()
            if answer2 == "walk":
                print("Ladi walks over to Jeffandy")
                answer3 = input("Does Jeffandy share that he's on a prayer call talking about Jesus, pretend like it's nothing, or compliment Ladi on her beauty \\n share, pretend or compliment? ").lower()
                if answer3 == "compliment":
                    print("Ladi thanks him for compliment and says good bye.\\n game over.")
                elif answer3 == "share":
                    print("They talk about life God and start what will be the most important friendship of their lives. YOU WIN!")
                    print(r\'\'\'
**********************************************
* HAPPILY EVER AFTER!               *
**********************************************
                    \'\'\')
                else:
                    print("The connection wasn't made. \\n game over.")
            elif answer2 == "stand":
                print("they never meet.. \\ngame over.")
            else:
                print("Ladi walks away.\\n game over")
        else:
            print("they never meet... \\n game over.")

        # Play Again Logic
        retry = input("\\nWould you like to play again? (yes/no): ").lower()
        if retry != "yes":
            print("Thanks for playing the Haiti Seoul Love Story! Goodbye.")
            break 

# Start the game
main_game()'''

# ============================================
# SESSION STATE INITIALIZATION
# ============================================

if 'game_stage' not in st.session_state:
    st.session_state.game_stage = 'start'
if 'answer1' not in st.session_state:
    st.session_state.answer1 = None
if 'answer2' not in st.session_state:
    st.session_state.answer2 = None
if 'answer3' not in st.session_state:
    st.session_state.answer3 = None

# ============================================
# GAME LOGIC
# ============================================

def reset_game():
    st.session_state.game_stage = 'start'
    st.session_state.answer1 = None
    st.session_state.answer2 = None
    st.session_state.answer3 = None

def main():
    # Main Title
    st.markdown("<h1 style='text-align: center; color: #dc143c; font-size: 3rem; margin-top: 20px;'>Haiti Seoul Love Story 💕</h1>", unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Game Introduction
    st.markdown("<div class='game-text'>Your mission is to start true love between Jeffandy and Ladi Seoul.</div>", unsafe_allow_html=True)
    st.markdown("<div class='game-text'>Make your choices wisely! 💕</div>", unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Game Flow
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        # Question 1
        if st.session_state.game_stage == 'start':
            st.markdown("### 🚪 Does Ladi turn left to patio or turn right to exit?")
            col_left, col_right = st.columns(2)
            
            with col_left:
                if st.button("⬅️ Turn Left", key="left", use_container_width=True):
                    st.session_state.answer1 = "left"
                    st.session_state.game_stage = 'question2'
                    st.rerun()
            
            with col_right:
                if st.button("➡️ Turn Right", key="right", use_container_width=True):
                    st.session_state.answer1 = "right"
                    st.session_state.game_stage = 'game_over_exit'
                    st.rerun()
        
        # Question 2
        elif st.session_state.game_stage == 'question2':
            st.success("Nice move! ✨")
            st.markdown("### 👫 Does Ladi walk to Jeffandy in corner or stand with friends?")
            col_walk, col_stand = st.columns(2)
            
            with col_walk:
                if st.button("🚶‍♀️ Walk to Jeffandy", key="walk", use_container_width=True):
                    st.session_state.answer2 = "walk"
                    st.session_state.game_stage = 'question3'
                    st.rerun()
            
            with col_stand:
                if st.button("🧍‍♀️ Stand with Friends", key="stand", use_container_width=True):
                    st.session_state.answer2 = "stand"
                    st.session_state.game_stage = 'game_over_stand'
                    st.rerun()
        
        # Question 3
        elif st.session_state.game_stage == 'question3':
            st.info("Ladi walks over to Jeffandy...")
            st.markdown("### 💬 What does Jeffandy do?")
            st.markdown("Does Jeffandy share that he's on a prayer call talking about Jesus, pretend like it's nothing, or compliment Ladi on her beauty?")
            
            col_s, col_p, col_c = st.columns(3)
            
            with col_s:
                if st.button("🙏 Share about Jesus", key="share", use_container_width=True):
                    st.session_state.answer3 = "share"
                    st.session_state.game_stage = 'win'
                    st.rerun()
            
            with col_p:
                if st.button("😶 Pretend it's nothing", key="pretend", use_container_width=True):
                    st.session_state.answer3 = "pretend"
                    st.session_state.game_stage = 'game_over_pretend'
                    st.rerun()
            
            with col_c:
                if st.button("😍 Compliment her beauty", key="compliment", use_container_width=True):
                    st.session_state.answer3 = "compliment"
                    st.session_state.game_stage = 'game_over_compliment'
                    st.rerun()
        
        # Win Condition
        elif st.session_state.game_stage == 'win':
            st.markdown("""
            <div class='win-message'>
                🎉 YOU WIN! 🎉<br>
                💕 HAPPILY EVER AFTER! 💕
            </div>
            """, unsafe_allow_html=True)
            st.success("They talk about life, God, and start what will be the most important friendship of their lives!")
            st.balloons()
            
            if st.button("🔄 Play Again", use_container_width=True):
                reset_game()
                st.rerun()
        
        # Game Over Conditions
        elif st.session_state.game_stage == 'game_over_exit':
            st.markdown("<div class='game-over'>💔 GAME OVER 💔<br>They never meet...</div>", unsafe_allow_html=True)
            if st.button("🔄 Try Again", use_container_width=True):
                reset_game()
                st.rerun()
        
        elif st.session_state.game_stage == 'game_over_stand':
            st.markdown("<div class='game-over'>💔 GAME OVER 💔<br>They never meet...</div>", unsafe_allow_html=True)
            if st.button("🔄 Try Again", use_container_width=True):
                reset_game()
                st.rerun()
        
        elif st.session_state.game_stage == 'game_over_compliment':
            st.markdown("<div class='game-over'>💔 GAME OVER 💔<br>Ladi thanks him for the compliment and says goodbye.</div>", unsafe_allow_html=True)
            if st.button("🔄 Try Again", use_container_width=True):
                reset_game()
                st.rerun()
        
        elif st.session_state.game_stage == 'game_over_pretend':
            st.markdown("<div class='game-over'>💔 GAME OVER 💔<br>The connection wasn't made.</div>", unsafe_allow_html=True)
            if st.button("🔄 Try Again", use_container_width=True):
                reset_game()
                st.rerun()
    
    st.markdown("---")
    
    # ============================================
    # CODE VIEWER SECTION
    # ============================================
    
    st.markdown("## 👨‍💻 Original Python Code")
    st.markdown("**Day 3 Project:** Showcasing nested if-else statements for a choose-your-own-adventure game")
    
    # Fake code editor with syntax highlighting
    st.markdown('<div class="code-header">📄 haiti-seoul-love-story.py</div>', unsafe_allow_html=True)
    
    # Split code into lines for line numbers
    code_lines = ORIGINAL_CODE.split('\n')
    
    code_html = '<div class="code-editor" style="white-space: pre; font-family: \'Courier New\', monospace;">'
    for i, line in enumerate(code_lines, 1):
        # Escape HTML characters first
        highlighted_line = line.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
        
        # Python keywords (blue)
        for keyword in ['def ', 'while ', 'if ', 'elif ', 'else:', 'break', 'return', 'True:', 'False']:
            highlighted_line = highlighted_line.replace(keyword, f'<span class="keyword">{keyword}</span>')
        
        # Function calls (yellow)
        highlighted_line = highlighted_line.replace('print(', '<span class="function">print</span>(')
        highlighted_line = highlighted_line.replace('input(', '<span class="function">input</span>(')
        highlighted_line = highlighted_line.replace('main_game()', '<span class="function">main_game</span>()')
        highlighted_line = highlighted_line.replace('.lower()', '.<span class="function">lower</span>()')
        
        # Strings - handle triple quotes and regular strings
        import re
        # Triple quoted strings
        highlighted_line = re.sub(r"('''.*?''')", r'<span class="string">\1</span>', highlighted_line, flags=re.DOTALL)
        highlighted_line = re.sub(r'(""".*?""")', r'<span class="string">\1</span>', highlighted_line, flags=re.DOTALL)
        # Regular strings
        highlighted_line = re.sub(r'(".*?")', r'<span class="string">\1</span>', highlighted_line)
        
        # Comments (green)
        if '#' in highlighted_line and '<span' not in highlighted_line.split('#')[1] if len(highlighted_line.split('#')) > 1 else False:
            parts = highlighted_line.split('#', 1)
            highlighted_line = parts[0] + '<span class="comment"># ' + parts[1] + '</span>'
        
        # Format line with proper number alignment
        code_html += f'<div style="display: flex;"><span class="line-number">{i:>3}</span><span>{highlighted_line}</span></div>'
    
    code_html += '</div>'
    st.markdown(code_html, unsafe_allow_html=True)
    
    # Project Info
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### 🎯 Learning Goals")
        st.markdown("""
        - Nested if-else logic
        - User input handling
        - Game state management
        - String manipulation
        """)
    
    with col2:
        st.markdown("### 🛠️ Technologies")
        st.markdown("""
        - Python 3.12
        - Streamlit
        - Session state
        - Custom CSS
        """)
    
    with col3:
        st.markdown("### 📅 Project Details")
        st.markdown("""
        - **Day:** 3 of 100
        - **Date:** December 2025
        - **Focus:** Control Flow
        - **Type:** Interactive Game
        """)

if __name__ == "__main__":
    main()
