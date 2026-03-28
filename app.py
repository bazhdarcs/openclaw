import os
import subprocess
import gradio as gr

# کارپێکردنی ئۆپن کڵاو لە پشتەوە
subprocess.Popen(["python", "-m", "openclaw"])

# دروستکردنی ڕووکارێکی سادە بۆ ئەوەی سێرڤەرەکە بە داگیرساوی بمێنێتەوە
def status():
    return "سکرتێرەکەت ئێستا ئۆنلاینە و لە تێلیگرامەوە چاوەڕێی فەرمانی تۆیە!"

demo = gr.Interface(fn=status, inputs=None, outputs="text", title="OpenClaw Worker")

if __name__ == "__main__":
    demo.launch()
