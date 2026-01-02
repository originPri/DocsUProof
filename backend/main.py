import os
import json
import sys
from pathlib import Path
from fastapi import FastAPI, File, UploadFile, HTTPException, Query, BackgroundTasks
from fastapi.responses import JSONResponse
from agent.agent import MainAgent
from agent.llm_adapters import MockLLMAdapter, GeminiLLMAdapter
from backend.schemas import Report
from uuid import uuid4
import shutil
import re
import docx
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import pdfplumber

