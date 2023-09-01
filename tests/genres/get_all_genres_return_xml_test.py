from api.genres_requests import GenresRequests
from assertpy import assert_that, soft_assertions
from lxml import etree


def test_get_all_genres_return_xml(regular_user_token):
    # Arrange
    response = GenresRequests().get_all_genres_return_xml_hardcoded(regular_user_token)

    # Act
    assert response.status_code == 200
    response_body = response.text
    
    with soft_assertions():
        # Verify
        tree = etree.fromstring(bytes(response_body, encoding='utf-8'))
        genres_names = [item[1].text for item in tree.xpath('//genre')]
        print(genres_names)
        assert_that(genres_names).contains('Action', 'Horror', 'Romance')

        genres_count = len(tree.xpath('//genre'))
        print(f"Genres count is: {genres_count}")
        assert_that(genres_count).is_greater_than(3)
    