from selenium import webdriver
import os
from configparser import ConfigParser
from selenium.webdriver.common.keys import Keys
import time
from behave import given, when, then, step
import googlebooksteps


# globals().update(locators)

# @step('{page} is launched')
# def step_impl(context,page):
#     context.helperfunc.open(page)
#     context.helperfunc.maximize()

@step('click on {Field}')
def step_impl(context,Field):
    context.helperfunc.find_element(Field).click()

@step('User enter {Field}')
def populate_data(context,Field):
    field_value_set=context.helperfunc.get_data(context.scenario.name,Field)
    context.helperfunc.fill_data(field_value_set)



@step('Submit')
def step_impl(context):
    context.execute_steps("When click on Submit")


@step('{Message} should displayed')
def step_impl(context,Message):
    context.helperfunc.find_element(Message)
