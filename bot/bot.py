import requests
from aiogram import Dispatcher, html, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext


dp = Dispatcher()

class Form(StatesGroup):
    name = State()
    group = State()


@dp.message(CommandStart())
async def command_start_handler(message: Message, state: FSMContext) -> None:
    await state.set_state(Form.name)
    await message.answer(f"Hello, what's your name?")


@dp.message(Form.name)
async def process_name(message: Message, state: FSMContext) -> None:
    await state.update_data(name=message.text)
    await state.set_state(Form.group)
    await message.answer(f"Nice to meet you, {html.bold(message.text)}!\nWhich group do you want to check?",)

@dp.message(Form.group)
async def process_group(message: Message, state: FSMContext) -> None:
    await state.update_data(group=message.text)
    # TODO: Add func for request server for group searching and processing data 
    await message.answer(f"Server answer\n")


#@dp.message(Command("find_group"))
#async def find_group_command(message: Message) -> None:
#    await message.answer(f"{Form.group} right?")
#    response = requests.get(url=f'http://localhost:8000/find?message={message.chat.id}')
#    await message.answer(f"ID:{response.content}")

