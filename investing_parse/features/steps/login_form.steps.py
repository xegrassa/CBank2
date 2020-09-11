from behave import *


@given('Пустые Логин и Пароль')
def step_impl(context):
    context.login = ""
    context.password = ""


@given('login "{login}"')
def step_impl(context, login):
    context.login = login


@given('password "{password}"')
def step_impl(context, password):
    context.password = password


@when('Пользователь пробует войти с текущим Логин и Паролем')
def step_impl(context):
    context.investing_login_form.input_login(context.login)
    context.investing_login_form.input_password(context.password)
    context.investing_login_form.submit()


@when('Открыть логин форму')
def step_impl(context):
    context.investing_login_form = context.investing_main_page.open_login_form()


@then('Открылась логин форма')
def step_impl(context):
    assert context.investing_login_form.is_open_login_form() is True


@then('Появилось предупреждение')
def step_impl(context):
    check_error = any((context.investing_login_form.is_email_error(),
                       context.investing_login_form.is_password_error(),
                       context.investing_login_form.is_authorization_error()))
    assert check_error is True
