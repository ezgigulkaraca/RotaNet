from ortools.constraint_solver import pywrapcp, routing_enums_pb2


def optimize_route(distance_matrix):
    """
    Google OR-Tools kullanarak en kısa rotayı hesaplar.

    Parameters
    ----------
    distance_matrix : numpy.ndarray

    Returns
    -------
    tuple
        (route, total_distance)
    """

    distance_matrix = distance_matrix.tolist()

    manager = pywrapcp.RoutingIndexManager(
        len(distance_matrix),
        1,      # Araç sayısı
        0       # Depo (başlangıç)
    )

    routing = pywrapcp.RoutingModel(manager)

    def distance_callback(from_index, to_index):

        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)

        return int(distance_matrix[from_node][to_node] * 1000)

    transit_callback_index = routing.RegisterTransitCallback(
        distance_callback
    )

    routing.SetArcCostEvaluatorOfAllVehicles(
        transit_callback_index
    )

    search_parameters = pywrapcp.DefaultRoutingSearchParameters()

    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC
    )

    solution = routing.SolveWithParameters(search_parameters)

    if solution is None:
        raise RuntimeError("Optimum rota bulunamadı.")

    index = routing.Start(0)

    route = []

    total_distance = 0

    while not routing.IsEnd(index):

        node = manager.IndexToNode(index)

        route.append(node)

        previous_index = index

        index = solution.Value(
            routing.NextVar(index)
        )

        total_distance += routing.GetArcCostForVehicle(
            previous_index,
            index,
            0
        )

    route.append(manager.IndexToNode(index))

    total_distance = total_distance / 1000

    return route, total_distance
