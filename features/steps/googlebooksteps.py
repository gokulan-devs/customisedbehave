from selenium import webdriver
import os
from configparser import ConfigParser
from selenium.webdriver.common.keys import Keys
import time
from behave import given, when, then

@given('Google page is launched')
def step_impl(context):
    context.helperfunc.open('https://books.google.co.in/')
    context.helperfunc.maximize()


@when('User navigates to Google books app')
def step_impl(context):
    pass


@then('Google book logo should appear in the page')
def step_impl(context):
    pass


@given('Google book page is on browser')
def step_impl(context):
    pass


@when('User enter Ponniyin Selvan in book search field')
def step_impl(context):
    pass


@when('user hit enter on search field')
def step_impl(context):
    pass


@then('Search results page should appear with link text ponniyin selvan')
def step_impl(context):
    pass
