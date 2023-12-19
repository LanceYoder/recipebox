public class recipe {
    String _name;
    int _rating;
    ingredienTag[] _tags;

    public recipe(String name, int rating, ingredienTag[] tags) {
        _name = name;
        _rating = rating;
        _tags = tags;
    }

    public String getName() {
        return _name;
    }

    public int getRating() {
        return _rating;
    }

    public ingredienTag[] getTags() {
        return _tags;
    }
}
