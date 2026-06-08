-- =========================================
-- INITIAL DATA INSERT
-- =========================================

-- ADMIN USER
INSERT INTO users (id, first_name, last_name, email, password, is_admin)
VALUES (
    'admin-001',
    'Admin',
    'User',
    'admin@hbnb.com',
    'hashed_password_here',
    1
);

-- SAMPLE USERS
INSERT INTO users (id, first_name, last_name, email, password, is_admin)
VALUES (
    'user-001',
    'John',
    'Doe',
    'john@doe.com',
    'hashed_password_here',
    0
);

-- AMENITIES
INSERT INTO amenities (id, name)
VALUES ('amenity-001', 'WiFi');

INSERT INTO amenities (id, name)
VALUES ('amenity-002', 'Pool');

INSERT INTO amenities (id, name)
VALUES ('amenity-003', 'Air Conditioning');

-- SAMPLE PLACE
INSERT INTO places (id, title, description, price, user_id)
VALUES (
    'place-001',
    'Beach House',
    'Beautiful house near the ocean',
    120.0,
    'user-001'
);

-- SAMPLE REVIEW
INSERT INTO reviews (id, text, rating, user_id, place_id)
VALUES (
    'review-001',
    'Amazing place!',
    5,
    'user-001',
    'place-001'
);

-- PLACE AMENITIES
INSERT INTO place_amenity (place_id, amenity_id)
VALUES ('place-001', 'amenity-001');

INSERT INTO place_amenity (place_id, amenity_id)
VALUES ('place-001', 'amenity-002');