import React from 'react'


function Row(props) {
    const booking = props.booking

    return (
        <tr>
            <td>{booking.flat_name}</td>
            <td>{booking.id}</td>
            <td>{booking.checkin}</td>
            <td>{booking.checkout}</td>
            <td>{booking.prev_booking_id || '-'}</td>
        </tr>
    )
}


function Ordering(props) {
    const ordering = props.ordering
    const setOrdering = props.setOrdering

    return (
        <div class="dropdown mb-1">
            <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
                Ordering
            </button>
            <ul class="dropdown-menu">
                <li>
                    <a 
                    class={"dropdown-item " + (ordering == 'flat,checkin' ? 'active' : '')} 
                    href="#"
                    onClick={() => setOrdering('flat,checkin')}
                    >
                        Flat, checkin
                    </a>
                </li>
                <li>
                    <a 
                    class={"dropdown-item " + (ordering == 'checkin' ? 'active' : '')} 
                    href="#"
                    onClick={() => setOrdering('checkin')}
                    >
                        Checkin
                    </a>
                </li>
            </ul>
        </div>
    )
}

export default function Table() {
    const [bookings, setBookings] = React.useState([])
    const [ordering, setOrdering] = React.useState('flat,checkin')

    function fetchBookings() {
        let url = `http://localhost:8000/api/bookings?ordering=${ordering}`
        fetch(url)
        .then(response => response.json())
        .then(response => setBookings(response))
    }

    React.useEffect(() => {
        fetchBookings()
    }, [ordering])

    return (
        <div>
            <Ordering ordering={ordering} setOrdering={setOrdering} />
            <table className='table table-striped'>
                <thead>
                    <tr>
                        <th scope="col">Flat name</th>
                        <th scope="col">ID</th>
                        <th scope="col">Checkin</th>
                        <th scope="col">Checkout</th>
                        <th scope="col">Previous booking  ID </th>
                    </tr>
                </thead>

                <tbody>
                    {bookings.map(booking => <Row booking={booking} />)}
                </tbody>
            </table>
        </div>
        
    )
}
