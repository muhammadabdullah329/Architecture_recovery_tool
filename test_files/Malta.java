public class Malta extends Citrus
{
	private double vitaminC;
	public Malta(int weight)
	{
		super(weight);
		vitaminC=0.02*super.getWeight();
		super.setVitaminc(vitaminC);
	}
	@Override
	public double getTotal()
	{
		return super.getTotal();
	}
}