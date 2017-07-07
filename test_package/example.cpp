#include <gsl/gsl>
#include <vector>

int main(int argc, char **argv)
{
  std::vector<int> vec = { 1, 2, 3 };
  gsl::span<int> data = gsl::make_span(vec);
}