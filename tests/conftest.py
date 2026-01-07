"""Pytest fixtures for pykabu tests"""

import pytest


@pytest.fixture
def sample_schedule_html():
    """Sample HTML for schedule page testing"""
    return '''
    <table id="SihyoT">
    <tr>
        <td class="date">1/8(水)</td>
        <td class="time">08:50</td>
        <td class="priority">★★★</td>
        <td class="event">日銀金融政策決定会合</td>
        <td class="result">-</td>
        <td class="expectation">-</td>
        <td class="last">-</td>
    </tr>
    <tr>
        <td class="time">14:00</td>
        <td class="priority">★★</td>
        <td class="event">景気動向指数</td>
        <td class="result">-</td>
        <td class="expectation">110.2</td>
        <td class="last">109.8</td>
    </tr>
    <tr>
        <td class="date">1/9(木)</td>
        <td class="time">21:30</td>
        <td class="priority">★★★★★</td>
        <td class="event">米雇用統計</td>
        <td class="result">256K</td>
        <td class="expectation">165K</td>
        <td class="last">212K</td>
    </tr>
    </table>
    '''
