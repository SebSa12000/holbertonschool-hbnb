## Entity-Relationship Diagram

```mermaid
erDiagram
    USER ||--o{ PLACES : own
    PLACES }|..|{ AMENITY : has_PLACE_AMENITY
    USER ||--o{ REVIEW : write
    PLACES ||--o{ REVIEW : receive
```