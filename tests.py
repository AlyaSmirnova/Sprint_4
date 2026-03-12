import pytest
import allure
from main import BooksCollector


@allure.suite('Unit tests for BooksCollector service')
class TestBooksCollector:

    @pytest.fixture
    def collector(self):
        collector = BooksCollector()
        yield collector
        collector.books_genre.clear()
        collector.favorites.clear()

    @allure.title('Add two books to the collection')
    def test_add_new_book_add_two_books(self, collector):
        with allure.step('Add "Pride and Prejudice and Zombie" and "What to do if your cat wants to kill you"'):
            collector.add_new_book('Pride and Prejudice and Zombie')
            collector.add_new_book('What to do if your cat wants to kill you')
        with allure.step('Verify that collection contains exactly 2 books'):
            assert len(collector.get_books_genre()) == 2

    @allure.title('Verify default empty state of the collection')
    def test_books_genre_empty_dictionary_is_true(self, collector):
        assert collector.books_genre == {}

    @allure.title('Verify default empty state of the favorites')
    def test_favorites_empty_list_is_true(self, collector):
        assert collector.favorites == []

    @allure.title('Verify predefined list of available genres')
    def test_genre_list_with_data_is_true(self, collector):
        assert collector.genre == ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']

    @allure.title('Verify predefined list of age rating genre')
    def test_genre_age_rating_list_with_data_is_true(self, collector):
        assert collector.genre_age_rating == ['Ужасы', 'Детективы']

    @allure.title('Cannot add the same book twice')
    def test_add_new_book_already_exists(self, collector):
        with allure.step('Add "To Kill a Mockingbird" twice'):
            collector.add_new_book('To Kill a Mockingbird')
            collector.add_new_book('To Kill a Mockingbird')
        with allure.step('Verify only one entry exists in the dictionary'):
            assert len(collector.books_genre) == 1
        
    @pytest.mark.parametrize('book_name, book_genre, expected_genre', [['Dune: Part 1', 'Фантастика', 'Фантастика'], ['Bridget Jones\'s Diary', 'Комедии', 'Комедии']])
    @allure.title('Set genre "{book_genre}" for book "{book_name}"')
    def test_set_book_genre_with_correct_name_and_valid_genre_is_success(self, book_name, book_genre, expected_genre, collector):
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, book_genre)
        assert collector.get_book_genre(book_name) == expected_genre

    @allure.title('Get genre by correct book name')
    def test_get_book_genre_with_correct_name_return_book_genre(self, collector):
        collector.add_new_book('Dune: Part 1')
        collector.set_book_genre('Dune: Part 1', 'Фантастика')
        assert collector.get_book_genre('Dune: Part 1') == 'Фантастика'

    @pytest.mark.parametrize('genre, expected_books', [['Фантастика', ['Dune: Part 1']], ['Комедии', ['Bridget Jones\'s Diary']]])
    @allure.title('Get list of books by specific genre: {genre}')
    def test_get_books_with_specific_genre_valid_names_and_genres_return_existing_genres(self, genre, expected_books, collector):
        with allure.step('Prepare test data (Dune and Bridget Jones)'):
            collector.add_new_book('Dune: Part 1')
            collector.set_book_genre('Dune: Part 1', 'Фантастика')
            collector.add_new_book('Bridget Jones\'s Diary')
            collector.set_book_genre('Bridget Jones\'s Diary', 'Комедии')
        with allure.step(f'Verify books for genre {genre}'):
            assert collector.get_books_with_specific_genre(genre) == expected_books

    @allure.title('Get all books genre dictionary (empty state)')
    def test_get_books_genre_empty_dictionary_is_true(self, collector):
        assert collector.get_books_genre() == {}

    @allure.title('Get all books genre dictionary (populated state)')
    def test_get_books_genre_not_empty_dictionary_is_true(self, collector):
        with allure.step('Add multiple books with genres'):
            collector.add_new_book('Blue Pills: A Positive Love Story')
            collector.set_book_genre('Blue Pills: A Positive Love Story', 'Комедии')
            collector.add_new_book('It')
            collector.set_book_genre('It', 'Ужасы')
        with allure.step("Verify the dictionary content"):
            books_in_dictionary = {'Blue Pills: A Positive Love Story': 'Комедии', 'It': 'Ужасы'}
            assert collector.get_books_genre() == books_in_dictionary


    @allure.title('Restricted genres are not included in children\'s list')
    def test_get_books_for_children_with_not_for_children_genres_is_restricted(self, collector):
        with allure.step('Add "Misery" (Horror genre)'):
            collector.add_new_book('Misery')
            collector.set_book_genre('Misery', 'Ужасы')
            assert collector.get_books_for_children() == []

    @pytest.mark.parametrize('book_name', ['Sharp Objects', 'The Silent Patient', 'The Chestnut Man'])
    @allure.title('Add book "{book_name}" to favorites')
    def test_add_book_in_favorites_book_in_books_genre_is_added(self, book_name, collector):
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        assert book_name in collector.favorites

    @pytest.mark.parametrize('book_name', ['Sharp Objects', 'The Silent Patient', 'The Chestnut Man'])
    @allure.title("Delete book from favorites")
    def test_delete_book_from_favorites_three_books_in_favorites_one_book_is_deleted(self, book_name, collector):
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        collector.delete_book_from_favorites('The Chestnut Man')
        assert 'The Chestnut Man' not in collector.favorites

    @allure.title('Get complete list of favorite books')
    def test_get_list_of_favorites_books_with_three_books_in_favorites_is_true(self, collector):
        with allure.step('Fill favorites with data'):
            collector.add_new_book('Sharp Objects')
            collector.add_new_book('It')
            collector.add_new_book('Blue Pills: A Positive Love Story')
            collector.add_book_in_favorites('Sharp Objects')
            collector.add_book_in_favorites('Blue Pills: A Positive Love Story')
        with allure.step('Verify favorites match exactly'):
            assert collector.get_list_of_favorites_books() == ['Sharp Objects', 'Blue Pills: A Positive Love Story']
