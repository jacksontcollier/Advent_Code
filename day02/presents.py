def calc_required_paper(present_input):
    
    total_paper_required = 0

    for present in present_input:
        dimensions = map(int, present.split('x'))

        side_a = dimensions[0] * dimensions[1]
        side_b = dimensions[0] * dimensions[2]
        side_c = dimensions[1] * dimensions[2]

        surface_area = (2 * side_a) + (2 * side_b) + (2 * side_c)
        wrapping_paper_required = surface_area + min(side_a, side_b, side_c)
        total_paper_required += wrapping_paper_required

    return total_paper_required

def calc_required_ribbon(presents_dimensions):
    
    total_ribbon_required = 0

    for present in presents_dimensions:
        dimensions = map(int, present.split('x'))
        dimensions.sort()
        total_ribbon_required += (2 * dimensions[0]) + (2 * dimensions[1])
        total_ribbon_required += dimensions[0] * dimensions[1] * dimensions[2]

    return total_ribbon_required
